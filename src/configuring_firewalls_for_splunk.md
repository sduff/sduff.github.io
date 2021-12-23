---
title: Configuring Firewalls for Splunk
date: 2017-01-01
tags: [splunk]
published: false
layout: default
series: splunk
---
# Configuring Firewalls for Splunk

Large Splunk deployments are often multi isntance deployments, possibly
spanning multiple data centres. Splunk instances need to communicate with each
other for a variety of reasons (data exchange, knowledge object replication,
running queries). 

>> Main comm port diagram

## Common ports openned in a Splunk deployment

|-+-+-+
| Service| Default/Typical Ports | Description |
| :-: | :-: | :-: |
| WebGUI | TCP/8000	| Default port for the Splunk Web interface. This should be disabled on all Splunk instances that are not search heads or used for Monitoring, by deploying a conf file such as XXX. |
| Recieving Splunk data | TCP/9997 | Indexers and forwarders that receive Splunk data use this port by default. It is possible for an instance to have multiple listening ports if required. |
| Management | TCP/8089 | This is the default management port. It can be used by the monitoring console, deployment server, deployer and/or cluster master. *This port can also be active on the search head to allow REST API queries* |
| Search Head Clustering Replication|	*TCP/8000* | No typical port is provided in Splunk documentation, but TCP/8080 is common. Used for Search Heads to syncronise knowledge objects, etc... |
| Indexer Clustering Replication|	TCP/??? | Used for clustered indexers to exchange replicated buckets |
| Syslog | UDP/514, TCP/514, TCP/1514	| Recieve Syslog traffic. Best practice is that syslog data is received by a 3rd party product such as syslog-ng or rsyslog, and Splunk configured to read the log files that are written.
|-|-|-|


In large enterprises, it is common to configure Splunk deployments to have a
"trusted core", comprising the search heads and indexers (and related
instances). Outside this core sits a "log aggregation" tier, which is
responsible for the collection of data. In this configuration, endpoints do not
communicate directly with the indexers, which may satisfy requirements such as
security zone models. If this is the case, the log aggregation tier usually
consists of heavy-weight or universal forwarders acting as log collectors, and
firewall rules established to allow only this tier to communicate with the
indexers.

Alternatively, enterprises may trust the entirity of their network, and may
choose to forgo the trusted core. This eliminates the need for a log
aggregation tier, although one may be used for the purposes of
resiliency/buffering, such as in the case of remote sites.


Search Heads Cluster
Search Head Unclustered
Deployer
Indexers clustered
Indexers non-clustered
Cluster Master
Log Aggregators
Universal Forwarders
Deployment Servers
Monitoring Console


While the communications between Splunk instances are well defined, there are
several popular firewall technologies that I've personally encountered at
engagements. Each firewall product is slightly different in how they are
configured to allow communication between instances.

# Local Firewalls

## IPTables

## RedHat firewalld

## SUSE Firewall2

## Other firewalls?

# Network Firewalls

## Cisco ASA

## Checkpoint


# References
* Splunk Firewall ports
* RHEL firewall config
