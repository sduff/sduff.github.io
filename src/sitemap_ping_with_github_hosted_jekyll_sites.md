---
title:
date: 2017-09-28
tags: [web]
published: true
layout: default
title: Sitemap pings for GitHub-hosted Jekyll sites
---

# Sitemap pings for GitHub-hosted Jekyll sites

## What is a sitemap?

According to a [news
release](https://googlepress.blogspot.com.au/2006/11/major-search-engines-unite-to-support_16.html)
by Google, Yahoo and Microsoft, a sitemap is *a free and easy way for
webmasters to notify search engines about their websites and be indexed more
comprehensively and efficiently*. Essentially, it is an XML document that
describes the various pages of a website, including their relative importance
and update frequency. Although these search engines have crawlers that will
index websites, pinging them with a sitemap might help guide their attention.

## Generating a sitemap with Jekyll

The easiest way to generate a sitemap in Jekyll is to use the [Jekyll Sitemap
plugin](https://github.com/jekyll/jekyll-sitemap). The plugin is [already
installed](https://help.github.com/articles/sitemaps-for-github-pages/) on
GitHub, so using it is as simple as including the following stanza in the
site's `_config.yaml`

```yaml
plugins:
  - jekyll-sitemap
```

For my website, I required a little more customisation, so created a file
called
[sitemap.xml](https://github.com/sduff/sduff.github.io/blob/master/sitemap.xml)
in the website root directory.

```html
{% raw %}---
layout: none
sitemap:
  exclude: 'yes'
---
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{% assign docs = site:docs | reverse docs %}
  {% for page in docs %}
    {% unless page.sitemap.exclude == "yes" %}
    <url>
      <loc>{{ site.url }}{{ page.url | remove: "index.html" }}</loc>
      {% if page.sitemap.lastmod %}
        <lastmod>{{ page.sitemap.lastmod | date: "%Y-%m-%d" }}</lastmod>
      {% elsif page.date %}
        <lastmod>{{ page.date | date_to_xmlschema }}</lastmod>
      {% else %}
        <lastmod>{{ site.time | date_to_xmlschema }}</lastmod>
      {% endif %}
      {% if page.sitemap.changefreq %}
        <changefreq>{{ page.sitemap.changefreq }}</changefreq>
      {% else %}
        <changefreq>monthly</changefreq>
      {% endif %}
      {% if page.sitemap.priority %}
        <priority>{{ page.sitemap.priority }}</priority>
      {% else %}
        <priority>0.3</priority>
      {% endif %}
    </url>
    {% endunless %}
  {% endfor %}
</urlset>{% endraw %}
```

These Jekyll directives generate the relevant XML code for each page in my web
site, generating a [valid sitemap.xml](http://simonduff.net/sitemap.xml) as the
output.

## Github webhooks

GitHub allows for webhooks to be attached to actions in a repository. In this
case, there should be a push to the various search engines to notify them that
the sitemap has been updated. To do so, the following URLs need to be called,
either by a `GET` or `POST` request.

```bash
https://www.google.com/webmasters/tools/ping?sitemap=http://simonduff.net/sitemap.xml
http://www.bing.com/ping?sitemap=http://simonduff.net/sitemap.xml
```

To configure, go to website repository's Settings section, and locate the
section called `Webhooks`.

![GitHub Settings Webhooks](/img/github_settings_webhooks.png "GitHub Settings Webhooks")

Configure webhooks for Google, Bing and any other search engine with sitemap submission facilities.

![Google Webhook](/img/github_webhook_google.png "Webhook configuration for Google")
![Bing Webhook](/img/github_webhook_bing.png "WebHook configuration for Bing")


After your next website push, you can check the responses of the two pings by
going to the individual webhook pages and checking the `responses`.
