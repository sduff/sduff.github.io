---
title: Splunk
date: 2017-06-21
tags: [splunk, technical]
layout: default
fav: true
series: splunk
---

# Splunk

I've been using Splunk for almost 10 years, after first being introduced to it
as a Security tool while I was working at a major Australian bank. So impressed
with the product, I joined the company, and have been a Professional Services
consultant with them ever since.

## What the Splunk?


*We Make Machine Data Accessible, Usable and Valuable to Everyone*
{: style="text-align: center"}

Splunk provides a mechanism for the collection of machine data information and
events, with a robust storage and analysis engine. Sitting on top of this is
a web front end that allows rapid exploration and development of dashboards and
alerts. The whole framework allows easy integration of 
[machine learning](https://splunkbase.splunk.com/app/2890/), 
[custom visualisations](http://docs.splunk.com/Documentation/Splunk/latest/AdvancedDev/CustomVizDevOverview) and 
[automated responses](https://www.splunk.com/en_us/solutions/solution-areas/security-and-fraud/adaptive-response-initiative.html).

We also have the [best T-shirts](https://www.co-store.com/splunk) 😉 

## Splunk-related pages on this site
<ul>
{% assign docs = site:docs | reverse docs %}
{% for page in docs %}{% if page.tags contains "splunk" and page.title != "Splunk"  %}
<li><a href="{{page.url}}">{{page.title}}</a></li>
{% endif %}{% endfor %}
</ul>

## Splunk Web Resources
* [Splunk Homepage](http://splunk.com) -- Splunk Homepage
* [Splunk Answers](https://answers.splunk.com/index.html) -- Questions and Answers!
* [SplunkBase](http://splunkbase.splunk.com) -- Thousands of Splunk apps
* [/r/Splunk](http://reddit.com/r/splunk) -- Splunk's home on reddit
* [GoSplunk](http://gosplunk.com/) -- Popular Splunk Queries
* [Big Book Of Splunk](http://www.bbosearch.com/) -- Even more Splunk Queries
* [Splunk Sizing Calculator](https://splunk-sizing.appspot.com/) -- Splunk Sizing Calculator for `indexes.conf`

## Splunk Blogs & Repositories
* [Splunk Blogs](https://www.splunk.com/blog/) -- Official Splunk Blog Posts
* [Ryan Faircloth](http://www.rfaircloth.com/)
* [Anthony Tellez](http://anthonygtellez.github.io/)
* [Duane Waddle](http://www.duanewaddle.com/)
* [Vladimir's GitHub](https://github.com/hire-vladimir/)
* [David Veuve](https://www.davidveuve.com/tech/)
