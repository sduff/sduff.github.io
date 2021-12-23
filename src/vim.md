---
title: Enough vim to be dangerous
date: 2017-10-09
tags: [dotfiles]
published: true
layout: default
---
# Enough `vim` to be dangerous

My occupation means that I'm usually working at a different customer from one
week to the next. There is little time to configure the operating environment
I'm working, so I have become some-what proficient at using `vim` using the
out-of-the-boxes defaults. Different distributions may ship with a different
set of defaults, but it is usually enough to be efficient by relying on the
`vim` basics.

## `vim` tips, tricks and shortcuts

<ul>
{% assign docs = site:docs | reverse docs %}
{% for page in docs %}{% if page.tags contains "vim" %}
<li><a href="{{page.url}}">{{page.title}}</a></li>
{% endif %}{% endfor %}
</ul>

## My local `.vimrc`

My `.vimrc` for my laptop is very minimally configured -- again, I've avoided
the use of plugins and major customisations, lest I develop a habit or muscle
memory relying on these.

```sh
" vimrc with minimal configuration

" Decoration
syntax on
set background=dark
colorscheme lucario
set ruler
set number numberwidth=4

" Tabbing
set expandtab
set shiftwidth=2 tabstop=2
set smartindent

" Searching
set ignorecase smartcase
set incsearch
set showmatch
set hlsearch
```

## References
* *Coming soon*
