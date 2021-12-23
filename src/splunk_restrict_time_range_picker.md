---
title: Restricting the Splunk Time Range Picker
date: 2017-07-06
tags: [splunk, ui]
published: true
layout: default
series: splunk
---
# Restricting the Splunk Time Range Picker

The [Splunk](/splunk) time range picker is a convinient widget for selecting froma
variety of different timeframes for a search. 

![Default Splunk time range picker](/img/splunk_time_range_picker_default.png "Default Splunk time range picker")

There are several ways that this timepicker can be customised, but they are
rather heavy-handed, in that they affect the whole app or system to which they
are applied.  As mentioned in the
[documentation](http://docs.splunk.com/Documentation/Splunk/latest/Search/Selecttimerangestoapply),
the list of Preset time ranges can be modified via editing the `times.conf`
file, either via the CLI or through the WebGUI, at 
`Settings > User Interface > Time Ranges`.
The other sections of the time range picker cannot be modified in this way however.

## Using CSS to hide time range picker elements

An alternative to this approach is to use CSS to hide the time range picker
elements that should not be available. A CSS file located in
`<app>/appserver/static/` can be included in a custom dashboard or form with the
line `<form stylesheet="filter.css">`. 

The following CSS provides a template for identifying and filtering the sections
and presets that are available by default.

```css
/* Hide whole sections 
 */
div[id^='presets_view'],
div[id^='relative_view'],
div[id^='realtime_view'],
div[id^='daterange_view'],
div[id^='dateandtimerange_view'],
div[id^='advanced_view'] {
	display: none;
}

/* Hide individual items 
 */
a[data-earliest="@d"][data-latest="now"], /* Today */
a[data-earliest="@w0"][data-latest="now"], /* Week to date */
a[data-earliest="@w1"][data-latest="now"], /* Business week to date */
a[data-earliest="@mon"][data-latest="now"], /* Month to date */
a[data-earliest="-1d@d"][data-latest="@d"], /* Yesterday */
a[data-earliest="-7d@w0"][data-latest="@w0"], /* Previous week */
a[data-earliest="-6d@w1"][data-latest="-1d@w6"], /* Previous business week */
a[data-earliest="-1mon@mon"][data-latest="@mon"], /* Previous month */
a[data-earliest="-15m"][data-latest="now"], /* Last 15 minutes */
a[data-earliest="-60m@m"][data-latest="now"], /* Last 60 minutes */
a[data-earliest="-4h@m"][data-latest="now"], /* Last 4 hours */
a[data-earliest="-24h@h"][data-latest="now"], /* Last 24 hours */
a[data-earliest="-7d@h"][data-latest="now"], /* Last 7 days */
a[data-earliest="-30d@d"][data-latest="now"] { /* Last 30 days */
	display: none;
}
```

The benefit of this approach is that entire sections can be hidden, and this
restriction can be done on a per-dashboard level, rather than at a per-app
level.

![Restricted Splunk time range picker](/img/splunk_time_range_picker_restricted.png "Restricted Splunk time range picker")

The downsides are that this is only works for custom dashboards and forms, and
that these presets are just  masked -- a crafty user could disable this CSS and
select these hidden items. However, Splunk provides sufficient restrictions as
part of its
[RBAC](https://docs.splunk.com/Documentation/Splunk/latest/Security/Aboutusersandroles)
model to limit users from doing long running or all time searches, if required.

You can grab an example app that demonstrates this configuration from
[https://github.com/sduff/restrict_timepicker](https://github.com/sduff/restrict_timepicker).
