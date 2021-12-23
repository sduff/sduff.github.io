---
title: A simple REST server in Python
layout: default
tags: [ code ]
date: 2017-04-18
---
# A simple REST server in Python

Using Python's `BaseHTTPServer`, its easy to build a very simple REST server, very
handy for prototyping. In no way should this be used in a production
environment! 

When visiting, via `GET` a page that doesn't exist, a very simple upload page
is presented. Revisiting the page will cause that file to be downloaded or
viewd. You need to manually (eg, using CURL) `POST` to the same page to upload
a new file to the same endpoint.

All data is stored in memory, and is deleted when the process stops. Like I
said, its not for production!  If you want some default or consistent data
present whenever you start the server, you can include it in the `endpoints`
definition in `main`.

The reason for the large number of headers is to handle
[CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing). The
settings in the file make the REST endpoint fairly accessible from anywhere.


```python
#!/usr/bin/env python

# Basic REST Server for prototyping

import sys, cgi, BaseHTTPServer, mimetypes

# Port to listen on
PORT = 1024

# List of endpoints
class endpoint:
    mimetype = ""
    content = ""
    def __init__(self,mimetype,content):
        self.mimetype = mimetype
        self.content = content
    
endpoints = {}

# The REST handler
class REST(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin","*")
        self.send_header("Access-Control-Allow-Methods","*")
        self.send_header("Access-Control-Allow-Headers","*")
        self.end_headers()

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin","*")
        self.send_header("Access-Control-Allow-Methods","*")
        self.send_header("Access-Control-Allow-Headers","*")
        self.end_headers()

    def do_GET(self):
        self.path = self.path.split("?",1)[0]
        if self.path in endpoints:
            ep = endpoints[self.path]
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin","*")
            self.send_header("Access-Control-Allow-Methods","*")
            self.send_header("Access-Control-Allow-Headers","*")
            self.send_header("Content-Type", ep.mimetype)
            self.end_headers()
            self.wfile.write(ep.content)

        else:
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin","*")
            self.send_header("Access-Control-Allow-Methods","*")
            self.send_header("Access-Control-Allow-Headers","*")
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write("""<html>
<body>
<form method="post" enctype="multipart/form-data" action=""")
            self.wfile.write('"'+self.path+'"')
            self.wfile.write(""">
<input type="file" name="upload"/><input type="submit" value="Submit">
</form>
</body>
</html>""")

    def do_POST(self):
        self.path = self.path.split("?",1)[0]
        try:
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            form = cgi.FieldStorage( fp=self.rfile, headers=self.headers, environ={'REQUEST_METHOD':'POST', 'CONTENT_TYPE':self.headers['Content-Type'], })
            content = form['upload'].file.read()
            filename = form['upload'].filename

            mt = mimetypes.guess_type(form["upload"].filename)[0] or "application/octet-stream"
            endpoints[self.path] = endpoint(mt,content)

            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin","*")
            self.send_header("Access-Control-Allow-Methods","*")
            self.send_header("Access-Control-Allow-Headers","*")
            self.send_header("Content-Type",mt)
            self.end_headers()
            self.wfile.write(content)
        except Exception as e:
            print sys.exc_info()
            self.send_response(500)
            self.send_header("Access-Control-Allow-Origin","*")
            self.send_header("Access-Control-Allow-Methods","*")
            self.send_header("Access-Control-Allow-Headers","*")
            self.end_headers()
            self.wfile.write(e)


if __name__ == '__main__':

    endpoints = {   "/": endpoint("text/plain","Hello world!"),
            "/bye.html": endpoint("text/html","<html><body>Bye</body></html>") 
    }

    print repr(endpoints)

    httpd = BaseHTTPServer.HTTPServer(("",PORT), REST)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
```

We can use `curl` for testing:
```bash
$ curl -F "upload=@./simon_duff.html" localhost:1024/owner
```

### References
* [https://www.spock.li/tutorials/rest-api](https://www.spock.li/tutorials/rest-api)
