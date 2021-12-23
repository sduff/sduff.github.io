---
title: Splunk Alert Script Template
date: 2017-07-17
tags: [splunk, python]
published: true
layout: default
series: splunk
---
# Splunk Alert Script

A [Splunk](/splunk) alert is a search that is periodically run, and if there are any
results, an *alert action* can be run. This is a custom script that can be used
to iterate over the search results and perform a task with the found fields.
This process is [documented](https://docs.splunk.com/Documentation/Splunk/latest/Alert/Configuringscriptedalerts), but the key takeaways are summarised on this page.

## Alert Script Arguments

When Splunk fires an alert action, there are several arguments that are passed
to the script. I usually ignore all of them, except for *argument 8*, which
contains a `gzip` `CSV` file containing the search results. The process is
usually to open this file and iterate over the results.

|-----+----------------------+-------|
| Arg | Environment Variable | Value |
| :-: | :------------------: | :---: |
| 0   |	SPLUNK_ARG_0 | Script name |
| 1	  | SPLUNK_ARG_1 | Number of events returned |
| 2   |	SPLUNK_ARG_2 | Search terms |
| 3   |	SPLUNK_ARG_3 | Fully qualified query string |
| 4   |	SPLUNK_ARG_4 | Name of report |
| 5   |	SPLUNK_ARG_5 | Trigger reason For example, *"The number of events was greater than 1."* |
| 6   |	SPLUNK_ARG_6 | Browser URL to view the report. |
| 7   |	SPLUNK_ARG_7 | Not used for historical reasons. |
| 8   |	SPLUNK_ARG_8 | File in which the results for the search are stored.  Contains raw results in gzip file format. |
|-----+----------------------+-------|

## Alert Script Code
The following template should be placed in the `$SPLUNK_HOME/bin/scripts/`
directory.

```python
import gzip
import csv

def openany(p):
	if p.endswith(".gz"):
		return gzip.open(p)
	else:
		return open(p)

results = sys.argv[8]
for row in csv.DictReader(openany(results)):
	# do something with row["field"]
```

This command can then be selected as a `Trigger Action` when saving or modifying
an alert.

![Splunk save as alert](/img/splunk_alert_action.png "Splunk save as alert")

## Advanced Alert Actions

The aforementioned script has actually been deprecated in preference of [Modular
Alerts](http://docs.splunk.com/Documentation/Splunk/6.4.2/AdvancedDev/ModAlertsIntro). These provide much more customisation features, but I often find this overkill.

Splunk also initiated the [Adaptive Response Initiative](https://www.splunk.com/en_us/solutions/solution-areas/security-and-fraud/adaptive-response-initiative.html) which allows for Splunk to integrate with other (mainly security related) 3rd party products, and allows for bidirectional communication between them. This is a great source for ideas for alert actions.

## Alert Script ideas
* Ticket Systems (*raise a ticket*)
* EMail (*send an email*)
* Anti Virus (*start a scan on a particular machine*)
* Firewall Rules (*isolate a compromised machine*)
* IOT devices (*think physical traffic lights, flags and sirens*)
* Enrichment (*Google a search query, write the results to a file which is indexed by Splunk*)
* Expect script (*ssh to a server and restart a hung process*)
