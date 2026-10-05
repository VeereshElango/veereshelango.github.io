# Veeresh Elango's website

This repository contains the source for [veereshelango.github.io](https://veereshelango.github.io/), a personal website and blog covering data science, machine vision, research, talks, and photography. It is built with Jekyll and the Minimal Mistakes theme, with custom pages, layouts, includes, styles, and scripts.

## Site sections

- **Blog:** articles in `_posts/`, published under `/posts/<title-slug>/` when categorized as `posts`.
- **Publications, talks, timeline, and profile pages:** maintained in `_pages/`.
- **Photobooks:** a gallery at `/photobooks/` and independent, static book sites under `photobooks/`.
- **Theme and site customizations:** `_config.yml`, `_data/`, `_includes/`, `_layouts/`, `_sass/`, and `assets/`.

The primary navigation is defined in [`_data/navigation.yml`](./_data/navigation.yml). Photobook gallery entries are defined in [`_data/photobooks.yml`](./_data/photobooks.yml).

## Tech stack

- Ruby, Bundler, Jekyll 3.9, and the `github-pages` gem (see [`Gemfile`](./Gemfile) and [`Gemfile.lock`](./Gemfile.lock)).
- The Minimal Mistakes remote theme, configured in [`_config.yml`](./_config.yml).
- Kramdown with GitHub Flavored Markdown for Markdown content.
- Python with Pillow for photobook image processing and book generation.
- Node.js's built-in test runner for the standalone photobook's HTML contract test.

## Run the site locally

Install the Ruby dependencies, then start Jekyll from the repository root:

```sh
bundle install
bundle exec jekyll serve --host 127.0.0.1
```

Open <http://127.0.0.1:4000/>. Jekyll watches site files and rebuilds during development. Stop the server with `Ctrl+C`.

To build without starting the server:

```sh
bundle exec jekyll build
```

The generated site is written to `_site/`; it is a build artifact and should not be edited by hand or committed.

### Ruby compatibility

The project uses Jekyll 3.9 and Liquid 4 through the GitHub Pages dependency set. These older versions rely on Ruby APIs removed in Ruby 4. If Jekyll reports missing `tainted?` or `untaint` methods, use a Ruby version compatible with the locked dependencies rather than modifying generated files or adding a project-specific runtime shim.

## Write a blog post

1. Add a dated Markdown file to `_posts/`, following the existing `YYYY-MM-DD-title.md` naming pattern.
2. Add YAML front matter. Posts intended for `/posts/` need `posts` in `categories`; use a suitable title, excerpt, tags, and optional header image.
3. Put post-specific images under `assets/images/posts/<post-slug>/` and refer to them with site-root paths such as `/assets/images/posts/<post-slug>/cover.jpg`.
4. Preview the post locally and check its layout, image paths, links, and mobile presentation.

The permalink format is configured in `_config.yml` as `/:categories/:title/`. Existing posts are useful examples of article tone, metadata, figures, and layouts.

## Photobooks

The gallery at `/photobooks/` is generated from `_data/photobooks.yml`. Each book has its own standalone directory at `photobooks/<slug>/`, published at `/photobooks/<slug>/`. The book's HTML, CSS, JavaScript, fonts, and photos use relative paths, so it does not need the Jekyll theme layout.

To publish another book:

1. Add its complete static site to `photobooks/<slug>/` with an `index.html` and relative asset paths. Keep the project source there too if it generates the HTML; the copy in this repository is the maintained version.
2. Prepare the photos for the web (requires Python and Pillow):

   ```sh
   python scripts/optimize_photos.py photobooks/<slug>/assets/photos
   ```

   The script applies EXIF rotation, removes other metadata (including GPS), keeps the colour profile, resizes large images in place to a 2000px long edge, and writes phone copies (up to 1200px wide or 1600px tall) to the sibling `assets/photos-1200/` directory. It modifies its input photos; keep full-resolution originals outside the repository and restore from them before processing again with different settings.
3. Add the slug, title, subtitle, description, date, and cover path to `_data/photobooks.yml`. The cover path is relative to the site root; use the `photos-1200` copy since gallery cards are small.
4. Preview the Jekyll site and check the gallery, book URL, images, navigation, and mobile page turns. Run any book-specific tests.

For *Stone and Light*, from `photobooks/stone-and-light/`, run:

```sh
python build_book.py
node --test html-contract.test.mjs
```

The builder requires Pillow (`PIL`). It emits `srcset`/`sizes` so phones can load smaller copies and defers interior photos (`data-src`/`data-srcset`) so `flipbook.js` only loads pages around the open one. The generated book HTML is checked by the contract test; the photos are not bundled into the test.

## Other development commands

The root [`package.json`](./package.json) contains legacy frontend asset commands:

```sh
npm install
npm run build:js
```

Use these only when intentionally rebuilding the theme's minified JavaScript assets. There is no root JavaScript test suite; the photobook test above uses Node's built-in runner.

## Repository map

```text
_posts/            Blog articles
_pages/            Static pages (profile, publications, talks, archives, photobooks)
_data/             Navigation, photobook records, and interface text
_includes/         Reusable Liquid templates and site-specific components
_layouts/          Jekyll page, post, archive, and taxonomy layouts
_sass/             Theme and site styles
assets/            Images, JavaScript, stylesheets, documents, and other static assets
photobooks/        Standalone photobook sites and their source
scripts/           Repository maintenance and media utilities
_site/             Generated Jekyll output (do not edit)
```

The root [`AGENTS.md`](./AGENTS.md) documents repository-specific conventions for contributors and coding agents.
