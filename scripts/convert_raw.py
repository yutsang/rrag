#!/usr/bin/env python3
"""
Convert raw source documents (PDF, PPTX, DOCX, XLSX, HTML) to markdown
using Microsoft's markitdown.

Why: The wiki's raw/courses/ directory is full of lecture PDFs and PPTX
decks. Markitdown gives us a clean markdown rendering that can be:
  1. Used as source material when authoring wiki pages
  2. Indexed directly as a "deep layer" alongside dify_export/ for RAG

Usage:
    python scripts/convert_raw.py                    # convert everything new
    python scripts/convert_raw.py --force            # re-convert all
    python scripts/convert_raw.py --dir raw/courses  # limit to subdir

Output:
    raw_converted/<mirrored path>.md
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from markitdown import MarkItDown
except ImportError:
    sys.exit("markitdown is not installed. Run: pip install -r scripts/requirements.txt")

REPO_ROOT = Path(__file__).parent.parent
RAW_ROOT = REPO_ROOT / "raw"
OUT_ROOT = REPO_ROOT / "raw_converted"

# File extensions markitdown handles well
SUPPORTED = {".pdf", ".pptx", ".docx", ".xlsx", ".html", ".htm", ".epub", ".md", ".txt"}
# Skip these — markdown already, or not worth indexing
SKIP_SUFFIXES = {".md"}  # raw/*.md gets passed through by the wiki pipeline already
SKIP_DIRS = {"assets"}   # raw/assets/ is images referenced by wiki pages


def should_convert(src: Path, dst: Path, force: bool) -> bool:
    if not dst.exists():
        return True
    if force:
        return True
    # Skip if destination is newer than source
    return src.stat().st_mtime > dst.stat().st_mtime


def convert_one(md: MarkItDown, src: Path, dst: Path) -> tuple[bool, str]:
    try:
        result = md.convert(str(src))
    except Exception as e:
        return False, f"{type(e).__name__}: {e}"

    text = (result.text_content or "").strip()
    if not text:
        return False, "empty output"

    # Prepend a small provenance header so the RAG index knows where this came from
    rel = src.relative_to(REPO_ROOT)
    header = f"---\nsource_file: {rel}\nconverter: markitdown\n---\n\n"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(header + text, encoding="utf-8")
    return True, f"{len(text.split()):,} words"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=None, help="Limit to a subdir of raw/ (e.g. raw/courses)")
    ap.add_argument("--force", action="store_true", help="Re-convert even if output is newer")
    args = ap.parse_args()

    root = Path(args.dir).resolve() if args.dir else RAW_ROOT
    if not root.exists():
        sys.exit(f"Source dir not found: {root}")

    md = MarkItDown()
    converted = skipped = failed = 0

    for src in sorted(root.rglob("*")):
        if not src.is_file():
            continue
        if src.suffix.lower() not in SUPPORTED or src.suffix.lower() in SKIP_SUFFIXES:
            continue
        if any(part in SKIP_DIRS for part in src.relative_to(REPO_ROOT).parts):
            continue

        rel = src.relative_to(REPO_ROOT)  # e.g. raw/courses/.../file.pdf
        # Strip the leading "raw/" so output lives at raw_converted/courses/...
        rel_no_raw = Path(*rel.parts[1:]) if rel.parts[0] == "raw" else rel
        dst = OUT_ROOT / rel_no_raw.with_suffix(".md")

        if not should_convert(src, dst, args.force):
            skipped += 1
            continue

        ok, msg = convert_one(md, src, dst)
        if ok:
            converted += 1
            print(f"  ✓ {rel}  ({msg})")
        else:
            failed += 1
            print(f"  ✗ {rel}  [{msg}]")

    print(f"\nDone. converted={converted}  skipped={skipped}  failed={failed}")
    print(f"Output: {OUT_ROOT}/")


if __name__ == "__main__":
    main()
