title: Simple REST API
layout: default
tags: [ python, tech, network ]
date: 2017-04-18
---
# Writing a simple REST API

Using Python's `BaseHTTPServer`, its easy to build a very simple REST API.

```python
```

We can use `curl` for testing:
```bash
$ curl -H 'Content-Type: application/json' -d '{ "msg": "Hello, World!" }' localhost:1024/endpoint
{"id":1}
```

### References
* https://www.spock.li/tutorials/rest-api
