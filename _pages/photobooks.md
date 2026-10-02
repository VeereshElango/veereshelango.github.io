---
title: Photobooks
permalink: /photobooks/
classes: wide
---

Photographic stories to explore, one page at a time.

<div class="photobook-gallery">
  {% for book in site.data.photobooks %}
    <article class="photobook-gallery__item">
      <a href="{{ '/photobooks/' | append: book.slug | append: '/' | relative_url }}">
        <img src="{{ book.cover | relative_url }}" alt="Cover photograph for {{ book.title | escape }}" loading="lazy">
        <h2>{{ book.title | escape }}</h2>
      </a>
      <p>{{ book.subtitle | escape }} · {{ book.date | date: "%Y" }}</p>
      <p>{{ book.description | escape }}</p>
    </article>
  {% endfor %}
</div>

<style>
  .photobook-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(min(100%, 260px), 1fr));
    gap: 2rem;
    margin-top: 2rem;
  }
  .photobook-gallery__item img {
    display: block;
    width: 100%;
    aspect-ratio: 4 / 5;
    object-fit: cover;
  }
  .photobook-gallery__item h2 { margin: 0.75rem 0 0; }
  .photobook-gallery__item p { margin: 0.5rem 0; }
</style>
