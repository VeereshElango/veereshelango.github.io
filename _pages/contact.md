---
permalink: /contact/
layout: splash
classes : wide
title: "Contact"

---

<style>
.pcard {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  max-width: 300px;
  margin: auto;
  text-align: center;
  margin-block-start: 1em;
}

.plabel {
  color: black;
  font-size: 18px;
}

.pbutton {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
  font-size: 18px;
}

a {
  text-decoration: none;
  color:black;
}

button:hover, a:hover {
  opacity: 0.7;
}
ul.no-bullets {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

</style>

{% assign author = page.author | default: page.authors[0] | default: site.author %}
{% assign author = site.data.authors[author] | default: author %}

<div class="pcard" itemscope itemtype="https://schema.org/Person">
    {% if author.avatar %}
    <div style="width:100%">
      {% if author.home %}
        <a href="{{ author.home | relative_url }}">
          <img src="{{ author.avatar | relative_url }}" alt="{{ author.name }}" itemprop="image">
        </a>
      {% else %}
        <img src="{{ author.avatar | relative_url }}" alt="{{ author.name }}" itemprop="image">
      {% endif %}
    </div>
  {% endif %}

  <div style="margin-top: 20px">
    {% if author.home %}
      <a href="{{ author_link }}"><h3 class="author__name" itemprop="name">{{ author.name }}</h3></a>
    {% else %}
      <h3 class="author__name" itemprop="name">{{ author.name }}</h3>
    {% endif %}
    {% if author.bio %}
      <div class="author__bio" style="font-size: 20px;" itemprop="description">
        {{ author.bio | markdownify }}
      </div>
    {% endif %}
  </div>
  <div style="margin: 24px 0;">
    <ul class="no-bullets">
        <li>
            <a href="https://wa.me/+919976043695" rel="nofollow noopener noreferrer">
                <i class="fab fa-fw fa-whatsapp" aria-hidden="true"></i>
                <span class="plabel">Whatsapp</span>
            </a>
        </li>
        <li>
            <a href="https://www.linkedin.com/in/veereshelango/" rel="nofollow noopener noreferrer">
                <i class="fab fa-fw fa-linkedin" aria-hidden="true"></i>
                <span class="plabel">Linkedin</span>
            </a>
        </li>
        <li>
            <a href="https://twitter.com/veereshelango" rel="nofollow noopener noreferrer">
                <i class="fab fa-fw fa-twitter-square" aria-hidden="true"></i>
                <span class="plabel">Twitter</span>
            </a>
        </li>
        <li>
            <a href="https://facebook.com/veereshelango" rel="nofollow noopener noreferrer">
                <i class="fab fa-fw fa-facebook-square" aria-hidden="true"></i>
                <span class="plabel">Facebook</span>
            </a>
        </li>
    </ul>
  </div>
  <p>
  <a href="{{ site.url }}{{ site.baseurl }}/assets/vcard.vcf?raw=1"><button class="pbutton">Save Contact</button></a></p>
</div>