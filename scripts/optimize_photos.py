#!/usr/bin/env python3
"""Prepare a photobook's photographs for the web.

    python scripts/optimize_photos.py photobooks/<slug>/assets/photos

For every JPEG under the given folder this:
  * applies the EXIF orientation and drops the remaining metadata (incl. GPS),
    keeping the ICC colour profile so colours stay accurate;
  * downsizes in place to LARGE_EDGE px on the long edge (desktop / retina);
  * writes a phone copy (SMALL_BOX) to a sibling ``<folder>-1200`` tree,
    used through ``srcset``.

Re-running is safe: photos already at or under LARGE_EDGE without EXIF
orientation are not re-encoded, and small copies are only regenerated when
missing or older than their source. Keep full-resolution originals outside
the repository.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from PIL import Image, ImageOps

LARGE_EDGE = 2000
LARGE_QUALITY = 85
# Phone copies: 1200px wide or 1600px tall, whichever binds first, so tall frames
# that fill a phone screen still have enough pixels on 3x displays.
SMALL_BOX = (1200, 1600)
SMALL_DIR_SUFFIX = "1200"
SMALL_QUALITY = 84
ORIENTATION_TAG = 274


def save(image: Image.Image, target: Path, box: tuple[int, int], quality: int, icc: bytes | None) -> None:
    resized = image.copy()
    resized.thumbnail(box, Image.LANCZOS)
    target.parent.mkdir(parents=True, exist_ok=True)
    resized.convert("RGB").save(
        target, "JPEG", quality=quality, optimize=True, progressive=True, icc_profile=icc
    )


def process(path: Path, small_path: Path) -> tuple[bool, bool]:
    with Image.open(path) as source:
        needs_large = max(source.size) > LARGE_EDGE or source.getexif().get(ORIENTATION_TAG, 1) != 1
        needs_small = needs_large or not small_path.exists() or small_path.stat().st_mtime < path.stat().st_mtime
        if not needs_small:
            return False, False
        icc = source.info.get("icc_profile")
        image = ImageOps.exif_transpose(source)
        image.load()

    if needs_large:
        save(image, path, (LARGE_EDGE, LARGE_EDGE), LARGE_QUALITY, icc)
    save(image, small_path, SMALL_BOX, SMALL_QUALITY, icc)
    return needs_large, True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("photos", type=Path, help="folder of photographs, e.g. photobooks/<slug>/assets/photos")
    args = parser.parse_args()

    photos_root = args.photos.resolve()
    if not photos_root.is_dir():
        print(f"Not a folder: {photos_root}", file=sys.stderr)
        return 1
    small_root = photos_root.with_name(f"{photos_root.name}-{SMALL_DIR_SUFFIX}")

    files = sorted(p for p in photos_root.rglob("*") if p.suffix.lower() in {".jpg", ".jpeg"})
    before = sum(p.stat().st_size for p in files)
    large_count = small_count = 0
    for path in files:
        large, small = process(path, small_root / path.relative_to(photos_root))
        large_count += large
        small_count += small

    after = sum(p.stat().st_size for p in files)
    small_total = sum(p.stat().st_size for p in small_root.rglob("*") if p.is_file()) if small_root.exists() else 0
    print(f"{len(files)} photos: {large_count} resized, {small_count} small copies written")
    print(f"{photos_root.name}: {before / 1e6:.1f} MB -> {after / 1e6:.1f} MB")
    print(f"{small_root.name}: {small_total / 1e6:.1f} MB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
