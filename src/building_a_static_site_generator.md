---
There are hundreds of static site generators https://jamstack.org/generators/ available. Enough already.

However, so many developers will often be lured by the siren call to write their own custom static site generator. Its either some feature that their current SSG misses, they find it too complex to tweak an SSG to create the output they want, or they just think they can do better than what is already out there.

However, it is not as straight forward as one might seem.

In all honesty, writing your own static site generator is a waste of time -- hence why I dubbed my own static site generator `waste`.

Countless revisions and updates, I confess I have spent more time writing and rewriting this generator than I have writing interesting articles.

This article aims to address

choosing a language
libraries
markdown
template libs - https://wiki.python.org/moin/TemplatingA
directory structure
static files
images
templates
parsing markdown, rendering html
one shot, one at a time, bulk load, dependencies, only rebuild as needed
managing metadata
   metadata for site
      tags, categories
   metadata for seo, amp, twitter, etc...
   microformats http://microformats.org/wiki/get-started
generating paths
themes/CSS
https://github.com/awesome-css-group/awesome-css
https://jamstackthemes.dev
Or you going with a CSS framework
level 0 - no css
https://www.cssbed.com/
https://github.com/dbohdan/classless-css
water, pure?
level 1 - css based themes
https://github.com/robsheldon/sscaffold-css/
https://github.com/milligram/milligram/wiki/Getting-Started
level 2 - css and lyout
https://picturepan2.github.io/spectre/layout/navbar.html
https://tachyons.io/components/text/large-paragraph/index.html
https://kbrsh.github.io/wing/
level 3 - bootstrap, etc...
extra features
OK, this is why so many people are here. How do you take advantage of all the extra functionality your theme has provided you.
Modifying the markdown parsers/render
code hilighting
SASS, postCSS
generating archive pages
   pagination
generating sitemaps
generating RSS
generating amp pages
comments?
RSS is not dead (its merely sleeping)
publishing?
   hooks into gh-pages, other jamstack?
building, packaging
Integrating with popular devop pipelines
pinging search engines
