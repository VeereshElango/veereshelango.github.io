# [My Blog](https://veereshelango.github.io/)

I have used [Minimal Mistakes Jekyll theme](https://mmistakes.github.io/minimal-mistakes/) for this blog.

## Photobooks

The gallery at `/photobooks/` is generated from `_data/photobooks.yml`. Each book
has its own standalone directory at `photobooks/<slug>/`, published at
`/photobooks/<slug>/`. The book's HTML, CSS, JavaScript, fonts, and photos use
relative paths, so it does not need the Jekyll theme layout.

To publish another book:

1. Add its complete static site to `photobooks/<slug>/` with an `index.html`
   and relative asset paths. Keep the project source there too if it generates
   the HTML; the copy in this repository is the maintained version.
2. Prepare the photos for the web (needs Pillow):

   ```
   python scripts/optimize_photos.py photobooks/<slug>/assets/photos
   ```

   This applies EXIF rotation, strips metadata (including GPS) while keeping
   the colour profile, resizes in place to 2000px on the long edge (JPEG q85,
   progressive), and writes phone copies (max 1200px wide or 1600px tall) to
   `assets/photos-1200/`. Re-running is safe. Keep full-resolution originals
   outside the repository; restore from them before re-running with new
   settings.
3. Add its slug, title, subtitle, description, date, and cover path to
   `_data/photobooks.yml`. The cover path is relative to the site root; use the
   `photos-1200` copy since gallery cards are small.
4. Preview the Jekyll site and check the gallery, book URL, images, navigation,
   and mobile page turns. Run any book-specific tests.

For *Stone and Light*, run `python build_book.py` and
`node --test html-contract.test.mjs` from `photobooks/stone-and-light/`.
The builder requires Pillow (`PIL`). It emits `srcset`/`sizes` so phones load
the smaller copies, and defers interior photos (`data-src`/`data-srcset`) so
`flipbook.js` only loads the pages around the open one. Its photos are about
18.5 MB (desktop) plus 10.8 MB (phone copies), down from 51.6 MB originals.
