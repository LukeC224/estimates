#!/usr/bin/env python3
"""Extract text and render pages from an architectural drawing set.

Text first to get keynotes, schedules and notes; then render the sheets that
matter and actually look at them. Keynote legends come out as text but the
bubbles placing them do not, so a takeoff from text alone will miss quantities.

    read_plans.py plans.pdf --index
    read_plans.py plans.pdf --text
    read_plans.py plans.pdf --text 19,20
    read_plans.py plans.pdf --render 19,20 --dpi 150 --out ./sheets
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import fitz  # pymupdf
except ImportError:
    sys.exit("pymupdf not installed. Run: pip3 install pymupdf")


def parse_pages(spec, page_count):
    """Turn '1,3,7-9' into [0,2,6,7,8]. None means every page."""
    if not spec:
        return list(range(page_count))
    pages = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            lo, hi = part.split("-", 1)
            pages.extend(range(int(lo) - 1, int(hi)))
        else:
            pages.append(int(part) - 1)
    bad = [p + 1 for p in pages if not 0 <= p < page_count]
    if bad:
        sys.exit(f"page(s) out of range 1-{page_count}: {bad}")
    return pages


# A sheet number standing alone in a title block: A101, D200, S-2, L-10, ID0.01.
# Requires a hyphen, 3 digits or a decimal, so a postal code ("M6P 2E6") won't match.
SHEET_RE = re.compile(
    r"^([A-Z]{1,2}(?:-\d{1,3}|\d{3})[A-Z]?|[A-Z]{1,3}\d\.\d{1,2})$"
)

# Boilerplate that repeats on every sheet and is never the title.
BOILERPLATE = re.compile(
    r"ISSUED RECORD|ARCHITECT|DRAWN|CHECKED|PROJECT|CLIENT|"
    r"^NO\.?$|^DATE$|^DESCRIPTION$|\.COM",
    re.I,
)

# Scale strings sit at the same font size as the title: '1:50', '1/4" = 1'-0"'.
SCALE_RE = re.compile(r'^[\d/]+\s*[:=]|["\']|^\d+:\d+$|^N$')


def title_block_spans(page, frac=0.22):
    """Text spans from the bottom-right corner, where the title block lives.

    Returns (text, font_size) pairs. Sheet number and title are the largest
    text in that corner, which holds up better across offices than pattern
    matching the whole page.
    """
    rect = page.rect
    clip = fitz.Rect(
        rect.x1 - rect.width * frac,
        rect.y1 - rect.height * frac,
        rect.x1,
        rect.y1,
    )
    spans = []
    data = page.get_text("dict", clip=clip)
    for block in data.get("blocks", []):
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                text = span["text"].strip()
                if text:
                    spans.append((text, round(span["size"], 1)))
    return spans


def read_title_block(page):
    """Best-effort (sheet_number, sheet_title). Either may be None."""
    spans = title_block_spans(page)
    if not spans:
        return None, None

    by_size = sorted(spans, key=lambda s: -s[1])
    sheet = next((t for t, _ in by_size if SHEET_RE.match(t)), None)

    # The title sits one font size below the sheet number, usually split across
    # spans, with the drawing scale sharing that size.
    sheet_size = next((sz for t, sz in spans if t == sheet), None)
    smaller = [sz for _, sz in spans if sheet_size is None or sz < sheet_size]
    title = None
    if smaller:
        title_size = max(smaller)
        parts = [
            t for t, sz in spans
            if sz == title_size
            and len(t) > 2
            and not BOILERPLATE.search(t)
            and not SCALE_RE.search(t)
        ]
        title = " ".join(parts).strip() or None
    return sheet, title


def cmd_index(doc):
    print(f"{doc.page_count} pages, {doc[0].rect.width:.0f}x{doc[0].rect.height:.0f} pt")
    print("(sheet/title read from the title block — verify against the drawing list)\n")
    for i, page in enumerate(doc):
        sheet, title = read_title_block(page)
        chars = len(page.get_text())
        print(f"{i + 1:>3}  {sheet or '?':<8} {chars:>6} chars  {(title or '')[:60]}")


def cmd_text(doc, pages):
    for i in pages:
        text = doc[i].get_text().strip()
        print(f"\n{'=' * 70}\nPAGE {i + 1}  ({len(text)} chars)\n{'=' * 70}")
        print(text)


def cmd_render(doc, pages, dpi, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    for i in pages:
        pix = doc[i].get_pixmap(dpi=dpi)
        path = out_dir / f"page-{i + 1:02d}.png"
        pix.save(path)
        print(f"{path}  {pix.width}x{pix.height}")
    print(f"\n{len(pages)} page(s) rendered. Read them — do not skip this step.")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf", type=Path)
    ap.add_argument("--index", action="store_true", help="list pages with guessed sheet numbers")
    ap.add_argument("--text", nargs="?", const="", metavar="PAGES", help="extract text layer")
    ap.add_argument("--render", metavar="PAGES", help="render pages to PNG")
    ap.add_argument("--dpi", type=int, default=120, help="render resolution (default 120)")
    ap.add_argument("--out", type=Path, default=Path("./sheets"), help="render output dir")
    args = ap.parse_args()

    if not args.pdf.exists():
        sys.exit(f"not found: {args.pdf}")
    if not (args.index or args.text is not None or args.render):
        ap.error("give one of --index, --text or --render")

    doc = fitz.open(args.pdf)

    if args.index:
        cmd_index(doc)
    if args.text is not None:
        cmd_text(doc, parse_pages(args.text, doc.page_count))
    if args.render:
        cmd_render(doc, parse_pages(args.render, doc.page_count), args.dpi, args.out)


if __name__ == "__main__":
    main()
