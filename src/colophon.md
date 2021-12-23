---
title: Colophon
layout: default
tags: [ website ]
date: 2017-09-21
series: website
---

# Colophon

*How does this marvelous web site work?*
{: style="text-align: center"}

## Site Generation and Hosting

This website it hosted on [GitHub Pages](http://pages.github.com) , which
integrates Jekyll, a static site generator.  You can find the source for the
site at [http://github.com/sduff/sduff.github.io](http://github.com/sduff/sduff.github.io).

Previously, I had written a custom site generator, called *WASTE*, but found I was
spending more time working on it than I did writing content for the site.
I abandoned it, but the [WASTE sources](http://github.com/sduff/waste) are
available, should you wish to see some hacked-together python code.

## Theme

I've slightly modified an existing Jekyll theme called
[Pixyll](https://github.com/sduff/pixyll) as I wasn't happy with the
readability of my homemade CSS.

For code highlighting, I [forked](https://github.com/sduff/lucario) a popular
text editor theme called [Lucario](https://github.com/raphamorim/lucario). This
is the same theme I use for my [vimrc and
terminal](https://github.com/sduff/dotfiles).

## Build

One particular aspect of this website is its connection to [Travis-CI](https://travis-ci.org/),
a continuous integration system. When I push new content to GitHub, Travis will
automatically attempt to build the site and verify any URLs are present and
correct. I'll be emailed the results of the build, on success or failure. I can
also include an icon on this page showing the build status.

[![Build Status](https://travis-ci.org/sduff/sduff.github.io.svg?branch=master)](https://travis-ci.org/sduff/sduff.github.io)
{: style="text-align: center"}

### Sitemap pings

[WASTE](http://github.com/sduff/waste), my homemade site generator, could
atomically ping Google and Microsoft Bing to alert them that a new version of
the site was available. There are actually several locations where we can hook
into the GitHub and Travis build process to perform the same tasks. These
mechanisms will be documented at a later stage.

## Analytics

I like data, and the site access logs are tracked using [Google
Analytics](http://analytics.google.com). Its probably overkill for my
requirements, which is just to reassure myself that someone is actually getting
value from my writing.

## Affiliate Links

This site may have some affiliate links, which means that when you click on a
link that I suggest, it may result in a commission for me. I'll only link to
items I actually use or support, and the possibility of a commission doesn't
sway my opinion of the product.

Seriously, we're probably talking a few cents here.

## Disclaimer

The postings on this site are my own and do not represent the 
position or opinions of my employer or its affiliates.

All data and information provided on this site is for informational purposes
only. I make no representations as to accuracy, completeness, currentness,
suitability, or validity of any information on this site and will not be liable
for any errors, omissions, or delays in this information or any losses,
injuries, or damages arising from its display or use. All information is
provided on an as-is basis.


