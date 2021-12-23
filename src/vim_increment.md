---
title: vim commands for bulk incrementing
date: 2018-02-24
tags: [vim]
published: true
layout: default
---

# `vim` commands for bulk incrementing

One common task required as part of Splunk administration was that of managing
the `serverclass.conf` file[^1]. This file contains a list of servers
that belong to a particular class, and all machines of that class receive a
particular set of configuration files.

A particularly frequent and some-what annoying task is adding and removing
servers from each class list. All servers in that list need be prefixed with
`whitelist.`*`X`*, where *`X`* is a consecutive number beginning at 0. When servers
are added or removed, potentially many entries require updating, and doing this
by hand could be error-prone.

Consider the following stanza; 2 machines have been decommissioned (commented
out in the file), and 3 new servers added to the end. At this stage, the list
would be rejected, as the entries do not begin at 0, there are gaps, and there
are duplicates.

```sh
[serverClass:windowsserver]
# whitelist.0 = 192.168.0.1 # Decomisioned !
whitelist.1 = 192.168.0.2
whitelist.2 = 192.168.0.3
# whitelist.3 = 192.168.0.4 # Decomisioned !
whitelist.4 = 192.168.0.5
whitelist.5 = 192.168.0.6
whitelist.6 = 192.168.0.7
whitelist.7 = 192.168.0.8
whitelist.8 = 192.168.0.9
whitelist.9 = 192.168.0.10
whitelist.10 = 192.168.0.11
whitelist.10 = 192.168.0.12 # New !
whitelist.10 = 192.168.0.13 # New !
whitelist.10 = 192.168.0.14 # New !
```

The following commands will renumber and sort the entries nicely.

```sh
let i=0
vipoj:'<,'>g/^whitelist.\d\+/s//\='whitelist.'.i/ | let i=i+1
gv:'<,'>!sort
```

```sh
[serverClass:windowsserver]
# whitelist.0 = 192.168.0.1 # Decomisioned !
# whitelist.3 = 192.168.0.4 # Decomisioned !
whitelist.0 = 192.168.0.2
whitelist.1 = 192.168.0.3
whitelist.10 = 192.168.0.13 # New !
whitelist.11 = 192.168.0.14 # New !
whitelist.2 = 192.168.0.5
whitelist.3 = 192.168.0.6
whitelist.4 = 192.168.0.7
whitelist.5 = 192.168.0.8
whitelist.6 = 192.168.0.9
whitelist.7 = 192.168.0.10
whitelist.8 = 192.168.0.11
whitelist.9 = 192.168.0.12 # New !
```

## Explanation

```sh
let i=0 {enter}
```

Create a new variable `i`, which will be used to count the valid lines.

```sh
vip
```

Visually select the entire paragraph.

```sh
oj
```
`o` to move the cursor to the other end of the block (the top), and `j` to move down once, thus skipping the stanza defining line.

```sh
:
```
Prepare to enter a command. `vim` will automatically insert `'<,'>`, which means to apply the command to the visual selection.

```sh
g/^whitelist.\d\+/
```
Globally perform a search where the start of the line (`^`) is followed by `whitelist.` and at least one number (`\d\+`). Because we look for `whitelist` at the begining of the line, the search ignores entries that have been commented out with a hash.

```sh
s//\='whitelist.'.i/
```
Substitute what is found by that search with `whitelist.` followed by the value of `i`.

```sh
| let i=i+1 {enter}
```
Increment the value of `i`.

```sh
gv
```
Repeat the previous visual selection.

```sh
:
```
Prepare to enter a command. Again, `vim` will automatically insert `'<,'>`.


```sh
:!sort {enter}
```
Sort the results.


#### Know a better sort? Please let me know!
[^1]: There's now a nice GUI for managing this file, but nothing beats getting your hands dirty and editing by hand!

## References
* [Power of G: vim wiki](http://vim.wikia.com/wiki/Power_of_g)
* [Making a list of numbers: vim wiki](http://vim.wikia.com/wiki/Making_a_list_of_numbers#Substitute_with_ascending_numbers)
