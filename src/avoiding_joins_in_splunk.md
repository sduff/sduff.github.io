---
title: Avoiding Joins in Splunk
date: 2017-01-01
tags: []
published: false
layout: default
series: splunk
---

```
index=_internal host=*opsanalytics* NOT host=esplu*opsanalytics* NOT host=*deploy* NOT host=*master*
   (source="/ebs_opt/splunk/var/log/splunk/mongod.log" "overcommit_memory") OR
   (source="/ebs_opt/splunk/var/log/splunk/splunkd.log" NOT component="DispatchManager"
   (
      ("My GUID is") OR
      ("Linux transparent hugepage support" NOT "enabled=\"never\" defrag=\"never\"") OR
      ("ulimit - Limit: user processes" NOT "409600 processes") OR
      ("ulimit - Limit: open files" NOT "819200 files")
     )
   ) earliest = -30d

| eval type_of_event = case(
   sourcetype="splunkd" AND (like(_raw,"%Linux transparent hugepage support%")), "thp_time",
   sourcetype="splunkd" AND (like(_raw,"%Limit: user processes%")), "ulimit_proc_time",
   sourcetype="splunkd" AND (like(_raw,"%Limit: open files%")), "ulimit_files_time",
   sourcetype="mongod", "overcommit_time",
   sourcetype="splunkd", "restart_time")
| stats latest(_time) as most_recent_time by type_of_event, host
| xyseries host type_of_event most_recent_time
| eval count=if('overcommit_time' &gt; 'restart_time' OR 'thp_time' &gt; 'restart_time' OR 'ulimit_proc_time' &gt; 'restart_time' OR 'ulimit_files_time' &gt; 'restart_time',"1","0")
| convert ctime("*_time") timeformat="%d/%m/%y %H:%M:%S"
| rename overcommit_time AS "Overcommit memory warning"
| rename thp_time AS "THP warning"
| rename ulimit_proc_time AS "Ulimit User Processes warning"
| rename ulimit_files_time AS "Ulimit Open Files warning"
| rename restart_time AS "Splunk restarted"| rename count as flag| sort -flag
```
