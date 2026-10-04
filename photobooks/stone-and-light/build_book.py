#!/usr/bin/env python3
"""Generate index.html for the Tuscany & Rome photobook.

The sequence below is the edit: cities stay in travel order (Florence, Siena,
Rome) and, inside each city, photographs are arranged for rhythm rather than
by capture time. Run from the book directory:

    python build_book.py
"""

from __future__ import annotations

import html
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent
PHOTOS = ROOT / "assets" / "photos"
# Produced by scripts/optimize_photos.py at the repository root.
SMALL_PHOTOS = ROOT / "assets" / "photos-1200"

PAGE_WIDTH = 460
PAGE_HEIGHT = 640

TITLE = "Stone and Light"
SUBTITLE = "Florence · Siena · Rome"
PHOTOGRAPHER = "Veeresh Elango"
COVER_PHOTO = ("Siena", "20260923_195315.jpg")

TRICOLOUR = '<span class="tricolour" aria-hidden="true"></span>'

# (city, filename, emphasis) — emphasis: "hero", "plate" or "quiet".
SEQUENCE: list[tuple[str, str, str]] = [
    # ---- Florence: three midday facades, marble against hard blue. ----
    ("Florence", "20260920_131949.jpg", "plate"),
    ("Florence", "20260920_135005.jpg", "hero"),
    ("Florence", "20260920_135811.jpg", "plate"),
    # ---- Siena: in through the gate, up to the light, down into night. ----
    ("Siena", "20260920_174735.jpg", "hero"),
    ("Siena", "20260920_175704~2.jpg", "plate"),
    ("Siena", "20260920_174056.jpg", "plate"),
    ("Siena", "20260922_083116.jpg", "plate"),
    ("Siena", "20260922_081448.jpg", "quiet"),
    ("Siena", "20260920_175222.jpg", "plate"),
    ("Siena", "20260922_082815.jpg", "hero"),
    ("Siena", "20260923_172504.jpg", "plate"),
    ("Siena", "20260920_180455.jpg", "quiet"),
    ("Siena", "20260920_181718.jpg", "hero"),
    ("Siena", "20260923_175245.jpg", "plate"),
    ("Siena", "20260923_175808.jpg", "plate"),
    ("Siena", "20260922_082212.jpg", "plate"),
    ("Siena", "20260920_191449.jpg", "quiet"),
    ("Siena", "20260920_191717.jpg", "hero"),
    ("Siena", "20260923_173425.jpg", "plate"),
    ("Siena", "20260920_190452.jpg", "hero"),
    ("Siena", "20260922_083646.jpg", "quiet"),
    ("Siena", "20260923_195315.jpg", "hero"),
    ("Siena", "20260923_195432.jpg", "plate"),
    ("Siena", "20260920_194904.jpg", "plate"),
    ("Siena", "20260920_194812.jpg", "plate"),
    ("Siena", "20260920_201852.jpg", "plate"),
    ("Siena", "20260925_081855.jpg", "hero"),
    ("Siena", "20260925_083930.jpg", "plate"),
    # ---- Rome: night arrival, a morning of angels, then the ceilings. ----
    ("Rome", "20260925_231110.jpg", "plate"),
    ("Rome", "20260925_232809.jpg", "quiet"),
    ("Rome", "20260925_231556.jpg", "hero"),
    ("Rome", "20260925_233516.jpg", "plate"),
    ("Rome", "20260926_084848.jpg", "hero"),
    ("Rome", "20260926_093044.jpg", "plate"),
    ("Rome", "20260926_092759.jpg", "plate"),
    ("Rome", "20260926_092954.jpg", "plate"),
    ("Rome", "20260926_131447.jpg", "quiet"),
    ("Rome", "20260926_114640.jpg", "plate"),
    ("Rome", "20260926_101345.jpg", "plate"),
    ("Rome", "20260926_101204.jpg", "hero"),
    ("Rome", "20260926_104906.jpg", "quiet"),
    ("Rome", "20260926_132411.jpg", "plate"),
    ("Rome", "20260926_131341.jpg", "hero"),
    ("Rome", "20260926_123201.jpg", "plate"),
    ("Rome", "20260926_122025.jpg", "hero"),
    ("Rome", "20260926_102503.jpg", "plate"),
    ("Rome", "20260926_134102.jpg", "hero"),
    ("Rome", "20260926_134223.jpg", "plate"),
    ("Rome", "20260926_134246.jpg", "plate"),
    ("Rome", "20260926_134326.jpg", "hero"),
]

ALT_TEXT: dict[str, str] = {
    "20260920_131949.jpg": "Green and white marble facade of Santa Maria Novella with a stone figure in front",
    "20260920_135005.jpg": "The brick dome and marble lantern of Florence Cathedral against a deep blue sky",
    "20260920_135811.jpg": "The rusticated wall and blue-shuttered windows of the Palazzo Vecchio above a marble statue",
    "20260920_174735.jpg": "A pointed brick gateway arch in the walls of Siena",
    "20260920_175704~2.jpg": "A figure silhouetted at the far end of a dark vaulted passage",
    "20260920_174056.jpg": "A narrow Siena lane with a wrought-iron sign and a window box of flowers",
    "20260922_083116.jpg": "A steep narrow street in morning shadow with a lamp and a strip of blue sky",
    "20260922_081448.jpg": "Warm brick housefronts in early sunlight along a Siena street",
    "20260920_175222.jpg": "A walled lane looking out over the rooftops of Siena",
    "20260922_082815.jpg": "Panorama of Siena rooftops and towers under a wide sky",
    "20260923_172504.jpg": "The town rising toward the cathedral, seen across terracotta roofs",
    "20260920_180455.jpg": "A carved pinnacle of the cathedral cut against plain blue sky",
    "20260920_181718.jpg": "The striped marble campanile and dome of Siena Cathedral",
    "20260923_175245.jpg": "The carved rose window of Siena Cathedral in low evening sun",
    "20260923_175808.jpg": "A slender cathedral pinnacle with a gargoyle against blue",
    "20260922_082212.jpg": "The she-wolf of Siena on her column, silhouetted against the sky",
    "20260920_191449.jpg": "Black and white study of a carved figure set into a brick wall",
    "20260920_191717.jpg": "Looking up from a palace courtyard to a rectangle of pale sky",
    "20260923_173425.jpg": "The Torre del Mangia seen at the end of a shadowed street",
    "20260920_190452.jpg": "The tip of the Torre del Mangia alone in a vast pale sky",
    "20260922_083646.jpg": "Pale blossom branching into an empty blue sky",
    "20260923_195315.jpg": "The Torre del Mangia and the Palazzo Pubblico at blue hour with the moon",
    "20260923_195432.jpg": "Lit windows of the Palazzo Pubblico across the Piazza del Campo at night",
    "20260920_194904.jpg": "An evening street hung with banners and warm lamplight",
    "20260920_194812.jpg": "A single street lamp burning in an empty night lane",
    "20260920_201852.jpg": "A lantern in a dark vaulted arcade",
    "20260925_081855.jpg": "A red scooter parked against a bare brick wall",
    "20260925_083930.jpg": "Two red rocking horses in a playground beside an old brick wall",
    "20260925_231110.jpg": "A small lit object in a niche inside a brick arch at night",
    "20260925_232809.jpg": "A Roman street at night with tail lights and lit facades",
    "20260925_231556.jpg": "A long illuminated colonnade glowing against a black sky",
    "20260925_233516.jpg": "A floodlit church dome and lantern at night",
    "20260926_084848.jpg": "Saint Peter's Basilica and the obelisk under morning cloud",
    "20260926_093044.jpg": "An angel statue on the bridge with the sun blazing behind it",
    "20260926_092759.jpg": "A bridge angel holding a cross, backlit by the sun",
    "20260926_092954.jpg": "A bridge angel carrying the crown of thorns against deep blue",
    "20260926_131447.jpg": "A baroque statue raised against a cloudless blue sky",
    "20260926_114640.jpg": "A bronze equestrian monument silhouetted on blue",
    "20260926_101345.jpg": "A marble triton wrestling in a baroque fountain",
    "20260926_101204.jpg": "A fountain putto riding a dolphin, carved in white marble",
    "20260926_104906.jpg": "Brick teeth and stucco on a terracotta-coloured Roman wall",
    "20260926_132411.jpg": "A cosmatesque mosaic band of interlocking stone circles",
    "20260926_131341.jpg": "A carved mask and garland on a Roman entablature",
    "20260926_123201.jpg": "The spiralling carved relief of Trajan's Column",
    "20260926_122025.jpg": "The Colosseum seen down the avenue in afternoon light",
    "20260926_102503.jpg": "A gilded dome oculus with a stained-glass centre",
    "20260926_134102.jpg": "The full length of a baroque painted church ceiling",
    "20260926_134223.jpg": "Figures tumbling through cloud in a baroque ceiling fresco",
    "20260926_134246.jpg": "A painted saint borne upward among angels on a church ceiling",
    "20260926_134326.jpg": "Swirling clouds and figures at the crown of a painted vault",
}

CHAPTERS: dict[str, dict[str, str]] = {
    "Florence": {
        "number": "One",
        "title": "Florence",
        "text": "An afternoon of facades. Green and white marble, a brick dome, "
        "a fortress wall — all of it held up into the same hard September blue.",
    },
    "Siena": {
        "number": "Two",
        "title": "Siena",
        "text": "Four days inside the walls. In through the gate and the dark passage, "
        "up through the lanes to the tower and the striped cathedral, down again "
        "into lamplight — and out the other side into an ordinary morning.",
    },
    "Rome": {
        "number": "Three",
        "title": "Rome",
        "text": "Arriving after dark, then a morning spent among angels, fountains and "
        "carved stone. It ends the way Rome insists you end: looking up.",
    },
}


def plate_class(path: Path, emphasis: str) -> str:
    """Pick a plate size from the photograph's own proportions and its role."""
    with Image.open(path) as source:
        width, height = ImageOps.exif_transpose(source).size
    ratio = width / height

    if ratio > 1.3:
        shape = "wide"
    elif ratio < 0.62:
        shape = "tall"
    else:
        shape = "upright"

    return f"plate {shape} {emphasis}"


# Largest plate box per shape (the "hero" paddings in style/book-style.css), as
# (box width, vertical padding) in page widths; CSS % padding is width-relative.
PLATE_BOX = {"wide": (0.95, 0.185), "upright": (0.88, 0.175), "tall": (0.90, 0.155)}


def width_fraction(width: int, height: int, shape: str) -> float:
    """Share of the page width a contained photo occupies at most."""
    box_width, vertical_padding = PLATE_BOX[shape]
    box_height = PAGE_HEIGHT / PAGE_WIDTH - vertical_padding
    return min(box_width, box_height * width / height)


def photo_attrs(city: str, name: str, fraction: float = 1.0, defer: bool = True) -> str:
    """Image attributes; deferred ones are hydrated near the open page by flipbook.js."""
    large = f"assets/photos/{city}/{name}"
    with Image.open(PHOTOS / city / name) as image:
        large_width, large_height = image.size
    dims = f'width="{large_width}" height="{large_height}"'
    prefix = "data-" if defer else ""
    small_path = SMALL_PHOTOS / city / name
    if not small_path.exists():
        return f'{prefix}src="{html.escape(large)}" {dims}'
    with Image.open(small_path) as image:
        small_width = image.width
    small = f"assets/photos-1200/{city}/{name}"
    # Slot width per layout (see styles.css): one page fills a narrow screen; on short
    # screens the page is height-bound (~60vh wide); otherwise a spread shows half each.
    sizes = f"(max-width: 909px) {fraction * 100:.0f}vw, (max-height: 711px) {fraction * 60:.0f}vh, {fraction * 50:.0f}vw"
    return (
        f'{prefix}src="{html.escape(large)}" '
        f'{prefix}srcset="{html.escape(small)} {small_width}w, {html.escape(large)} {large_width}w" '
        f'sizes="{sizes}" {dims}'
    )


def photo_page(entry: tuple[str, str, str], side: str, folio: int) -> str:
    city, name, emphasis = entry
    alt = html.escape(ALT_TEXT.get(name, f"Photograph from {city}"))
    cls = plate_class(PHOTOS / city / name, emphasis)
    with Image.open(PHOTOS / city / name) as image:
        fraction = width_fraction(*image.size, cls.split()[1])
    return (
        f'<article class="book-page art-page paper {side}" aria-label="{city} photograph {folio}">'
        f'<figure class="{cls}"><img {photo_attrs(city, name, fraction)} alt="{alt}" decoding="async"></figure>'
        f'<p class="credit">{PHOTOGRAPHER}</p>'
        f'<p class="folio">{city} · {folio:02d}</p>'
        f"</article>"
    )


def blank_page(side: str) -> str:
    return (
        f'<article class="book-page art-page paper {side}" aria-label="Blank page">'
        f'<p class="credit">{PHOTOGRAPHER}</p></article>'
    )


def chapter_page(city: str, side: str) -> str:
    meta = CHAPTERS[city]
    return (
        f'<article class="book-page art-page paper {side}" aria-label="{meta["title"]} chapter opening">'
        f'<div class="chapter">{TRICOLOUR}<p class="chapter-number">{meta["number"]}</p>'
        f'<h2>{meta["title"]}</h2><p class="chapter-text">{meta["text"]}</p></div>'
        f'<p class="credit">{PHOTOGRAPHER}</p>'
        f"</article>"
    )


def build_pages() -> list[str]:
    pages: list[str] = []

    def add(markup_for_side) -> None:
        # Index 0 is the cover; verso pages are odd, recto pages even.
        side = "verso" if len(pages) % 2 else "recto"
        pages.append(markup_for_side(side))

    city, name = COVER_PHOTO
    cover_alt = html.escape(ALT_TEXT[name])
    pages.append(
        '<article class="book-page art-page cloth cover recto" data-density="hard" aria-label="Front cover">'
        f'<figure class="cover-art"><img {photo_attrs(city, name, defer=False)} alt="{cover_alt}" fetchpriority="high"></figure>'
        '<span class="cover-scrim" aria-hidden="true"></span>'
        '<span class="cover-band" aria-hidden="true"></span>'
        f'<h2 class="cover-title">{TITLE}</h2>'
        '<span class="cover-rule" aria-hidden="true"></span>'
        f'<p class="cover-subtitle">{SUBTITLE}</p>'
        f'<p class="cover-by"><span>Photographs by</span>{PHOTOGRAPHER}</p>'
        '<p class="cover-foot">SEPTEMBER 2026</p>'
        "</article>"
    )
    add(lambda s: f'<article class="book-page art-page endpaper {s}" aria-label="Endpaper"></article>')
    add(
        lambda s: f'<article class="book-page art-page paper {s}" aria-label="Title page">'
        f'<div class="title-block">{TRICOLOUR}<h2>{TITLE}</h2><p>{SUBTITLE}</p>'
        f'<p class="by"><span>Photographs by</span>{PHOTOGRAPHER}</p>'
        "<p>Fifty photographs, September 2026</p></div></article>"
    )

    counters = {city: 0 for city in CHAPTERS}
    current_city: str | None = None

    for entry in SEQUENCE:
        city = entry[0]
        if city != current_city:
            # Open every chapter on a left-hand page facing its first photograph,
            # with at least one blank leaf as a pause between chapters.
            if current_city is not None:
                add(blank_page)
            while len(pages) % 2 == 0:
                add(blank_page)
            add(lambda s, c=city: chapter_page(c, s))
            current_city = city
        counters[city] += 1
        add(lambda s, e=entry, f=counters[city]: photo_page(e, s, f))

    while len(pages) % 2 == 0:
        add(blank_page)

    add(
        lambda s: f'<article class="book-page art-page paper {s}" aria-label="Colophon">'
        f'<div class="colophon">{TRICOLOUR}<p>{TITLE}</p>'
        "<p>Florence, Siena and Rome — September 2026.</p>"
        f'<p class="by"><span>All photographs by</span>{PHOTOGRAPHER}</p>'
        '<p class="small-print">Fifty photographs, reproduced unaltered and in full. '
        "Set in Source Serif 4. Arrow keys, drag or the corner of a page turn the leaves.</p>"
        "</div></article>"
    )
    add(lambda s: f'<article class="book-page art-page endpaper {s}" aria-label="Endpaper"></article>')

    side = "verso" if len(pages) % 2 else "recto"
    pages.append(
        f'<article class="book-page art-page cloth {side}" data-density="hard" aria-label="Back cover">'
        f'<span class="back-mark">{TITLE}</span>'
        f'<p class="back-by"><span>Photographs by</span>{PHOTOGRAPHER}</p>'
        f"{TRICOLOUR}</article>"
    )
    return pages


def main() -> None:
    pages = build_pages()
    body = "\n        ".join(pages)
    document = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{TITLE} — {SUBTITLE}</title>
  <meta name="description" content="Fifty photographs from a journey through Florence, Siena and Rome.">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
<main class="room">
  <header class="book-header">
    <a href="../">← Photobooks</a><h1>{TITLE}</h1>
    <span id="orientation">Open spread</span>
  </header>
  <section class="stage" aria-label="Interactive photo book">
    <div class="book-rig">
      <div id="book" class="book" data-page-width="{PAGE_WIDTH}" data-page-height="{PAGE_HEIGHT}">
        {body}
      </div>
    </div>
  </section>
  <footer class="controls" aria-label="Book controls">
    <button id="previous" type="button" aria-label="Previous page">←</button>
    <div class="status" aria-live="polite"><span id="page-status">Cover</span><small>Drag, arrow keys, or F for full screen</small></div>
    <button id="next" type="button" aria-label="Next page">→</button>
  </footer>
</main>
<script src="vendor/page-flip.browser.js"></script>
<script src="flipbook.js"></script>
</body>
</html>
"""
    (ROOT / "index.html").write_text(document, encoding="utf-8")
    print(f"index.html written with {len(pages)} leaves")


if __name__ == "__main__":
    main()
