---
title: Visualising Service Status with Emoji
layout: default
tags: [ splunk, viz ]
date: 2018-11-09
no_ads: true
---

# Visualising Service Status with Emoji

Splunk dashboards can host a variety of different visualisation types, from
maps and charts to 3D globes. Its also possible to use something as simple as
Emoji.  Inspired by [this app](https://splunkbase.splunk.com/app/4273/), I
propose the use of the following mapping of severity to emoji.

[Splunk
ITSI](https://www.splunk.com/en_us/software/it-service-intelligence.html) is a
service monitoring tool that can intelligently assign severities to services
based on underlying infrastructure or application issues. There are also many
other severity and status categorisations, as listed in the references on this
page.

|Severity|Recommended Emoji|Other Applicable Emoji|Reason for Recommendation|
|: - :|:--------------:| -- | -- |
|Critical|💀|☠️ 😡🤬🔥💩❌🛑⛔️📛🚫|Significantly different than all other recommended emoji|
|High|😵|😳🤪😠😠😷🤒🤕🤢🤮⚠️😱😤😢😭😦😧😨😩🤯😬😰|Open mouth and X'd eyes lead to quick identification|
|Medium|😥|😣😮🤐😯😪😫😖😞😟|Emoji with sweat and frown|
|Low|🤔|🤨🤨😐😑|Emoji with hand and straight mouth|
|Normal|😃|😁😀😄😉😊😋🙂😎👍|Big eyes and big smile|
|Maintenance|🔨|🤞🔧⚒ 🛠⛏|Hammer is significantly different|
|Informational|ℹ️|🧐 🤓|They made an emoji specifically for *Information*, let's use it|

## Using Emoji in your Splunk query
`| rangemap field=load 💀=90-100 😵=80-89 😥=70-79 🤔=50-69 😃=0-49`

## Example dashboard
```
<dashboard>
  <label>Emoji-Monitor</label>
  <row>
    <panel>
      <single>
        <search>
          <query>
| makeresults | eval load=random()%100
| rangemap field=load 💀=90-100 😵=80-89 😥=70-79 🤔=50-69 😃=0-49 default=🔨
| fields range
          </query>
          <refresh>1s</refresh>
        </search>
        <option name="underLabel">indexer01</option>
      </single>
    </panel>
  </row>
</dashboard>
```

![Emoji Monitoring Splunk Dashboard](/img/emoji-monitoring.gif)

## References
* [StatusPage.io](https://help.statuspage.io/knowledge_base/topics/overview-1)
* [NetCool](https://www.ibm.com/support/knowledgecenter/en/SSSHTQ_7.4.0/com.ibm.netcool_OMNIbus.doc_7.4.0/omnibus/wip/user/concept/omn_usr_el_eventseveritylevels.html)
* [Syslog Event Severity](https://en.wikipedia.org/wiki/Syslog#Severity_level)
* [Java Logging Framework/Apache Commons](https://en.wikipedia.org/wiki/Java_logging_framework#Severity_level)
