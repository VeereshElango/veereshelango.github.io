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
2. Add its slug, title, subtitle, description, date, and cover path to
   `_data/photobooks.yml`. The cover path is relative to the site root.
3. Preview the Jekyll site and check the gallery, book URL, images, navigation,
   and mobile page turns. Run any book-specific tests.

For *Stone and Light*, run `python build_book.py` and
`node --test html-contract.test.mjs` from `photobooks/stone-and-light/`.
The builder requires Pillow (`PIL`). Its published photos are about 49 MB;
use appropriately sized exports for future books and keep original photos
outside the published directory.
