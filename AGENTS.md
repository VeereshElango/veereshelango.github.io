# Repository guidance

## Project overview

- This is the Jekyll source for `veereshelango.github.io`, a personal website built on Jekyll 3.9, GitHub Pages gems, and the Minimal Mistakes remote theme.
- The site includes blog posts, static pages, profile and research content, and standalone photobooks. Read the root `README.md` for commands and workflows before changing those systems.
- The configured permalink pattern is `/:categories/:title/`. A post categorized as `posts` is published at `/posts/<title-slug>/`.

## Working safely

- Inspect the relevant files and current Git status before editing. The worktree may contain user-authored or untracked work; preserve it and do not revert or overwrite it.
- Make focused changes that serve the request. Follow the existing Liquid, YAML, Markdown, HTML, CSS, JavaScript, Python, and Jekyll patterns in the touched area.
- Do not edit `_site/`, `.jekyll-cache/`, `.sass-cache/`, or other generated output by hand. Change its source and rebuild instead.
- Do not change dependency versions, theme configuration, deployment settings, or build tooling unless the request requires it.
- Do not commit changes unless asked.
- Do not expose credentials, personal contact details, private photo originals, or other sensitive material in documentation, generated pages, logs, or external services. Ask before publishing new identifiable people or private media.

## Content conventions

### Posts and pages

- Add articles as dated Markdown files in `_posts/`, with clear YAML front matter and categories, tags, and excerpts consistent with nearby posts.
- Keep post-specific media in `assets/images/posts/<slug>/`; use site-root URLs in Jekyll front matter and article content.
- Preserve the site's established first-person voice for personal articles. Link to primary sources when useful, and ensure external links support the text.
- Add or update static content in `_pages/`; update `_data/navigation.yml` only when the requested change affects primary navigation.
- Use the configured Jekyll layouts and includes instead of duplicating existing shared components.

### Photobooks and media

- Each book is a standalone site under `photobooks/<slug>/`; the gallery metadata belongs in `_data/photobooks.yml`. Keep the book's internal links and media paths relative so its static pages remain self-contained.
- Treat photo processing as destructive: `scripts/optimize_photos.py` rewrites oversized or EXIF-oriented input JPEGs in place, removing metadata including GPS. Preserve originals, inspect the exact target directory, and only run this tool when requested.
- Keep accessibility and performance in mind: use meaningful image alt text, appropriately sized images, and the established lazy-loading behavior.

## Validation

- For Jekyll content or configuration changes, run `bundle exec jekyll build`; when useful, start `bundle exec jekyll serve --host 127.0.0.1` and verify the affected URL and assets.
- Jekyll 3.9/Liquid 4 are incompatible with Ruby 4's removal of `tainted?` and `untaint`. If the build fails with those methods, report the environment compatibility failure; do not add a repository shim or alter dependencies unless requested.
- For `photobooks/stone-and-light/`, run `python build_book.py` only when its generated book needs updating, then run `node --test html-contract.test.mjs` for the book HTML contract.
- For changes to the root JavaScript build inputs, use the relevant root `npm` script in `package.json`. Do not run unrelated asset rebuilds.
- For documentation-only changes, check Markdown structure and links in context; a full site build is not required unless the docs affect a generated page or a documentation check exists.
- In the final summary, state what changed and which checks ran. Report blockers and test failures explicitly.
