---
title: Network Connectivity with Python
layout: default
tags: [ splunk, code ]
date: 2017-06-07
---

# Using Python for testing network connectivity

More and more Linux distributions have stopped shipping with basic networking
tools such as `telnet` installed by default. `ping` is still available
(sometimes), but to test if a server can communicate with another server on
a particular port is now a challenge.

However, I find `python` is installed more-often-than-not, and ships with
networking libraries that one can use for connectivity purposes. The following
snippet checks for connectivity, in this case, HTTPS (443) to `google.com`.

```python
$ python
import socket
socket.socket().connect(("google.com",443))
```

Run it, and you'll either get an exception thrown when connectivity fails, or no
exception for a successful connection.

**N.B.** this won't confirm application firewalls won't block traffic, but as
a basic connectivity test, this works fine.

Here is also a snazzy one liner to make a `bash` function if you need to run
a large number of checks

```bash
c() { python <<<"import socket; s=socket.socket(); s.settimeout(5); s.connect(('$1',$2)) ; print 'Connection'"; }
```

And then use it in the following manner.

```bash
$ c google.com 443
$ c google.com 22
```

If you're testing an internal network, set the timeout to something lower than
3 seconds, while if you're testing a WAN or internet server, set it to a higher
value.

## Connectivity testing with Splunk's inbuilt Python

I normally need to do connectivity tests as part of installing [Splunk](/splunk),
which usually ships with `python` (although not with the Universal Forwarder).
The python interpreter can be accessed from the command line with
```bash
/opt/splunk/bin/splunk cmd python
``` 

So the one liner becomes
```bash
c() { /opt/splunk/bin/splunk cmd python <<<"import socket; s=socket.socket(); s.settimeout(5); s.connect(('$1',$2)) ; print 'Connection'"; }
```
