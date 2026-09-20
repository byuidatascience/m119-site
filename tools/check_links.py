#!/usr/bin/env python3
"""Find every link in site/**/*.qmd and check whether it actually resolves.

Checks two kinds of links:
  - External (http/https): sent a real HTTP request; flagged if the final
    status is 4xx/5xx or the request errors out (timeout, DNS, TLS, ...).
  - Internal (relative paths, e.g. ../projects/foo.qmd, class-2.html#Prep):
    resolved against the filesystem. A ".html" target is treated as valid
    if either the literal file exists (pre-rendered pages, e.g. under
    projects/m119-docs/) or a sibling ".qmd" with the same name exists
    (pages Quarto renders itself). Anchor targets (#id) are checked
    against the destination source when it's a local .qmd.

Run manually:  uv run python tools/check_links.py
Run in CI:     python tools/check_links.py  (uv venv activated)

Examples:
  python tools/check_links.py                    # check everything, write report
  python tools/check_links.py --external-only     # skip filesystem checks
  python tools/check_links.py --internal-only     # skip HTTP checks (fast, no network)
  python tools/check_links.py --file class-5.qmd  # only files matching this glob
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urldefrag

import requests
import urllib3

# We deliberately retry with verify=False for domains whose cert chain this
# checker's trust store doesn't have (see check_external) — don't spam
# stderr with a warning about a choice already being made on purpose.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

REPO_ROOT = Path(__file__).parent.parent
SITE_DIR = REPO_ROOT / "site"
DEFAULT_REPORT = REPO_ROOT / "link_check_report.csv"

SKIP_SCHEMES = ("mailto:", "tel:", "javascript:", "data:")

# Markdown link/image targets: [text](target) or ![alt](target). The target
# allows one level of nested (...) so URLs like Wikipedia's
# ..._(2000%E2%80%93present) don't get truncated at the first ")".
MD_LINK_RE = re.compile(r'!?\[[^\]]*\]\(((?:[^()\s]|\([^()]*\))+)(?:\s+"[^"]*")?\)')
# HTML href="..."/src="..." (single or double quoted)
HTML_ATTR_RE = re.compile(r"""(?:href|src)\s*=\s*(["'])(.*?)\1""")
# Bare http(s) URLs anywhere else (R code url("..."), autolinks <https://...>,
# plain-text URLs, footnote refs, etc.) — same one-level-nested-parens
# allowance as MD_LINK_RE.
BARE_URL_RE = re.compile(r'https?://(?:[^\s"\'()<>\]]|\([^()]*\))+')

TRAILING_PUNCT = ".,;:!?)"

# id="foo" / {#foo} / <a id="foo"> anchor definitions inside a .qmd
ANCHOR_DEF_RE = re.compile(r'(?:id\s*=\s*"([^"]+)"|\{#([A-Za-z0-9_-]+)\})')

HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
FENCE_RE = re.compile(r"^\s*```")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)


def strip_html_comments(text: str) -> str:
    """Blank out <!-- ... --> spans (can be multi-line) while keeping line
    numbers intact, so a placeholder link sitting in a comment (e.g. the
    "add the new QR code" TODO) isn't reported as a real broken link."""
    def blank(m: re.Match) -> str:
        return "\n" * m.group(0).count("\n")
    return HTML_COMMENT_RE.sub(blank, text)


def slugify_heading(text: str) -> str:
    """Approximate Pandoc's auto-generated heading id algorithm closely
    enough to check #heading-slug links (e.g. unit2.html#maximum-
    likelihood-method-for-f_6 from '### Maximum Likelihood Method for $f_6$')."""
    text = re.sub(r"\$([^$]*)\$", r"\1", text)  # unwrap $math$, keep content (e.g. f_6)
    text = re.sub(r"[*`]", "", text)  # drop emphasis/code markup characters
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)  # links -> link text
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    text = re.sub(r"-+", "-", text)
    return text


def collect_anchors(text: str) -> set[str]:
    anchors = {a or b for a, b in ANCHOR_DEF_RE.findall(text)}
    for m in HEADING_RE.finditer(text):
        anchors.add(slugify_heading(m.group(2)))
    return anchors


@dataclass
class LinkOccurrence:
    file: Path
    line: int
    url: str


@dataclass
class Result:
    occurrence: LinkOccurrence
    kind: str  # "external" | "internal"
    status: str  # "OK" | "BROKEN" | "SKIP"
    detail: str


def clean_target(raw: str) -> str:
    """Strip Quarto/Pandoc attribute suffixes and stray trailing punctuation."""
    target = raw.strip()
    # Drop a trailing {...} attribute block glued onto the URL, e.g.
    # (url){target="_blank"} already excluded by MD_LINK_RE's `\)` stop,
    # but bare-URL matches can pick up trailing punctuation (end of a
    # sentence, or a wrapping "(see https://example.com)").
    while target and target[-1] in TRAILING_PUNCT:
        if target[-1] == ")" and target.count("(") >= target.count(")"):
            break  # closing paren is balanced by one inside the URL itself
        target = target[:-1]
    return target


def find_qmd_files(pattern: str | None) -> list[Path]:
    files = sorted(SITE_DIR.rglob("*.qmd"))
    files = [f for f in files if "_site" not in f.parts and ".quarto" not in f.parts]
    if pattern:
        files = [f for f in files if f.match(pattern) or pattern in f.name]
    return files


def extract_links(path: Path) -> list[LinkOccurrence]:
    occurrences: list[LinkOccurrence] = []
    raw_text = path.read_text(encoding="utf-8", errors="replace")
    text = strip_html_comments(raw_text)

    in_fence = False
    for lineno, line in enumerate(text.splitlines(), start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue

        seen_on_line: set[str] = set()

        def add(raw: str):
            target = clean_target(raw)
            if not target or target in seen_on_line:
                return
            seen_on_line.add(target)
            occurrences.append(LinkOccurrence(file=path, line=lineno, url=target))

        # Bare URLs matter even inside fenced code (e.g. R's
        # read.csv(url("https://..."))), so always check for those.
        for m in BARE_URL_RE.finditer(line):
            add(m.group(0))

        if in_fence:
            continue  # markdown/HTML link syntax inside a fence is a syntax demo, not a real link

        # Inline `code spans` are almost always showing syntax
        # (e.g. "Use `[Link text](url)`"), not a real link — drop them
        # before scanning for markdown/HTML link syntax.
        line_sans_inline_code = INLINE_CODE_RE.sub("", line)
        for m in MD_LINK_RE.finditer(line_sans_inline_code):
            add(m.group(1))
        for m in HTML_ATTR_RE.finditer(line_sans_inline_code):
            add(m.group(2))
    return occurrences


def is_external(url: str) -> bool:
    return url.startswith("http://") or url.startswith("https://")


def is_skippable(url: str) -> bool:
    return url.startswith(SKIP_SCHEMES) or url.startswith("#")


def _request(session: requests.Session, url: str, timeout: float, headers: dict, verify: bool) -> requests.Response:
    resp = session.head(url, timeout=timeout, allow_redirects=True, headers=headers, verify=verify)
    if resp.status_code >= 400 or resp.status_code == 405:
        # Some servers reject HEAD (405) or lie to it; confirm with GET.
        resp = session.get(url, timeout=timeout, allow_redirects=True, headers=headers, stream=True, verify=verify)
    return resp


def check_external(session: requests.Session, url: str, timeout: float) -> tuple[str, str]:
    headers = {"User-Agent": "Mozilla/5.0 (compatible; m119-link-checker/1.0)"}

    # A 429 means "ask again later", not "this doesn't exist" — retry a
    # couple times with backoff before giving up.
    for attempt in range(3):
        try:
            resp = _request(session, url, timeout, headers, verify=True)
        except requests.exceptions.SSLError:
            # Some institutional domains (e.g. *.byui.edu) serve a cert
            # chain this checker's trust store doesn't have, even though
            # the resource itself is genuinely reachable (verified
            # separately: the OS keychain trusts it, e.g. via curl). Retry
            # once without verification so a real 404/5xx there still gets
            # flagged, instead of every such domain being reported broken.
            try:
                resp = _request(session, url, timeout, headers, verify=False)
            except requests.exceptions.RequestException as exc2:
                return "BROKEN", f"{type(exc2).__name__}: {exc2}"
            if resp.status_code >= 400:
                return "BROKEN", f"HTTP {resp.status_code} (TLS cert also unverified by this checker)"
            return "OK", f"HTTP {resp.status_code} (TLS cert not verified by this checker — spot-check manually)"
        except requests.exceptions.RequestException as exc:
            return "BROKEN", f"{type(exc).__name__}: {exc}"

        if resp.status_code == 429 and attempt < 2:
            time.sleep(3 * (attempt + 1))
            continue
        break

    status = resp.status_code
    if status == 429:
        # Still rate-limited after retries — that's a statement about our
        # request volume, not about whether the link is dead. Flag it for a
        # manual/solo re-check rather than reporting a false broken link.
        return "RATE_LIMITED", f"HTTP 429 after retries — re-check manually (run with --workers 1)"
    if status >= 400:
        return "BROKEN", f"HTTP {status}"
    return "OK", f"HTTP {status}"


def resolve_internal(base_file: Path, target: str) -> tuple[str, str]:
    path_part, frag = urldefrag(target)
    if not path_part:
        # Pure "#anchor" same-page link — trust it, not worth parsing here.
        return "OK", "same-page anchor (unchecked)"

    if path_part.startswith("/"):
        candidate = (SITE_DIR / path_part.lstrip("/")).resolve()
    else:
        candidate = (base_file.parent / path_part).resolve()

    resolved_file: Path | None = None
    if candidate.is_dir():
        for index_name in ("index.qmd", "index.html"):
            if (candidate / index_name).exists():
                resolved_file = candidate / index_name
                break
    elif candidate.exists() and candidate.is_file():
        resolved_file = candidate
    elif candidate.suffix == ".html":
        sibling_qmd = candidate.with_suffix(".qmd")
        if sibling_qmd.exists():
            resolved_file = sibling_qmd

    if resolved_file is None:
        try:
            shown = candidate.relative_to(REPO_ROOT)
        except ValueError:
            shown = candidate
        return "BROKEN", f"no such file: {shown}"

    if frag and resolved_file.suffix == ".qmd":
        text = resolved_file.read_text(encoding="utf-8", errors="replace")
        anchors = collect_anchors(text)
        if frag not in anchors:
            return "BROKEN", f"anchor #{frag} not found in {resolved_file.relative_to(REPO_ROOT)}"

    return "OK", f"resolved to {resolved_file.relative_to(REPO_ROOT)}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--file", help="Only check .qmd files matching this glob/substring")
    parser.add_argument("--external-only", action="store_true", help="Skip filesystem (internal link) checks")
    parser.add_argument("--internal-only", action="store_true", help="Skip HTTP (external link) checks")
    parser.add_argument("--timeout", type=float, default=10.0, help="Per-request timeout in seconds (default: 10)")
    parser.add_argument("--workers", type=int, default=5, help="Concurrent HTTP requests (default: 5)")
    parser.add_argument("--out", type=Path, default=DEFAULT_REPORT, help=f"CSV report path (default: {DEFAULT_REPORT})")
    args = parser.parse_args()

    files = find_qmd_files(args.file)
    if not files:
        print("No .qmd files matched.", file=sys.stderr)
        return 1

    all_occurrences: list[LinkOccurrence] = []
    for f in files:
        all_occurrences.extend(extract_links(f))

    external: list[LinkOccurrence] = []
    internal: list[LinkOccurrence] = []
    skipped = 0
    for occ in all_occurrences:
        if is_skippable(occ.url):
            skipped += 1
        elif is_external(occ.url):
            external.append(occ)
        else:
            internal.append(occ)

    results: list[Result] = []

    if not args.external_only:
        for occ in internal:
            status, detail = resolve_internal(occ.file, occ.url)
            results.append(Result(occ, "internal", status, detail))

    if not args.internal_only and external:
        # Check each distinct URL once, then fan the result back out to every
        # occurrence — the same broken link is often pasted in several files.
        unique_urls = sorted({occ.url for occ in external})
        print(f"Checking {len(unique_urls)} distinct external URLs "
              f"({len(external)} occurrences) with {args.workers} workers...")
        url_results: dict[str, tuple[str, str]] = {}
        with requests.Session() as session:
            with ThreadPoolExecutor(max_workers=args.workers) as pool:
                future_to_url = {
                    pool.submit(check_external, session, url, args.timeout): url
                    for url in unique_urls
                }
                done = 0
                for future in as_completed(future_to_url):
                    url = future_to_url[future]
                    url_results[url] = future.result()
                    done += 1
                    if done % 25 == 0 or done == len(unique_urls):
                        print(f"  {done}/{len(unique_urls)} checked")
        for occ in external:
            status, detail = url_results[occ.url]
            results.append(Result(occ, "external", status, detail))

    results.sort(key=lambda r: (str(r.occurrence.file), r.occurrence.line))

    broken = [r for r in results if r.status == "BROKEN"]
    rate_limited = [r for r in results if r.status == "RATE_LIMITED"]

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["file", "line", "kind", "status", "url", "detail"])
        for r in results:
            writer.writerow([
                r.occurrence.file.relative_to(REPO_ROOT),
                r.occurrence.line,
                r.kind,
                r.status,
                r.occurrence.url,
                r.detail,
            ])

    print(f"\n{len(all_occurrences)} links found ({skipped} skipped: mailto/tel/etc.)")
    print(f"{len(results)} checked -> {len(broken)} broken, {len(rate_limited)} rate-limited (re-check needed)")
    print(f"Report written to {args.out.relative_to(REPO_ROOT)}")

    if broken:
        print("\nBroken links:")
        for r in broken:
            rel = r.occurrence.file.relative_to(REPO_ROOT)
            print(f"  {rel}:{r.occurrence.line}  [{r.kind}]  {r.occurrence.url}  ({r.detail})")

    if rate_limited:
        print("\nRate-limited (not necessarily broken — re-run with --workers 1 to confirm):")
        for r in rate_limited:
            rel = r.occurrence.file.relative_to(REPO_ROOT)
            print(f"  {rel}:{r.occurrence.line}  [{r.kind}]  {r.occurrence.url}")

    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
