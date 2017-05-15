#!/usr/bin/env python

# REST my case
# Simon Duff <sduff@splunk.com>
# Basic REST Server for prototyping

import cgi, BaseHTTPServer
import mimetypes

import time # for usage, need to save the current timestamp

# Port to listen on
PORT = 1025

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
        self.send_header("Access-Control-Allow-Headers","x-splunk-form-key")
        self.end_headers()

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin","*")
        self.send_header("Access-Control-Allow-Methods","*")
        self.send_header("Access-Control-Allow-Headers","x-splunk-form-key")
        self.end_headers()

    def do_GET(self):
        self.path = self.path.split("?",1)[0]
        if self.path == "/usage/":
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin","*")
            self.send_header("Access-Control-Allow-Methods","*")
            self.send_header("Access-Control-Allow-Headers","x-splunk-form-key")
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            content  = "["
            first = True
            for k,v in endpoints.iteritems():
                if k.startswith("/usage/"):
                    if not first:
                        content += ','
                        first = False
                    content += '\n  "path":"'
                    content += k
                    content += '", "timestamp":"'
                    content += v.content
                    content += '"'
            content += "\n]"
            self.wfile.write(content)
        elif self.path.startswith("/usage/"):
            now = str(int(time.time()))
            endpoints[self.path] = endpoint("text/plain",now)
            ep = endpoints[self.path]

            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin","*")
            self.send_header("Access-Control-Allow-Methods","*")
            self.send_header("Access-Control-Allow-Headers","x-splunk-form-key")
            self.send_header("Content-Type", ep.mimetype)
            self.end_headers()
            self.wfile.write(ep.content)

        elif self.path in endpoints and not self.path.startswith("/_new_/") :
            ep = endpoints[self.path]
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin","*")
            self.send_header("Access-Control-Allow-Methods","*")
            self.send_header("Access-Control-Allow-Headers","x-splunk-form-key")
            self.send_header("Content-Type", ep.mimetype)
            self.end_headers()
            self.wfile.write(ep.content)

        else:
            if self.path.startswith("/_new_/"):
                p = self.path[6:]
            else:
                p = self.path
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin","*")
            self.send_header("Access-Control-Allow-Methods","*")
            self.send_header("Access-Control-Allow-Headers","x-splunk-form-key")
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write("""<html>
<body>
<form method="post" enctype="multipart/form-data" action=""")
            self.wfile.write('"'+p+'"')
            self.wfile.write(""">
<input type="file" name="upload"/><input type="submit" value="Submit">
</form>
</body>
</html>""")

    def do_POST(self):
        self.path = self.path.split("?",1)[0]
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = cgi.FieldStorage(
                fp=self.rfile, 
                headers=self.headers,
                environ={'REQUEST_METHOD':'POST', 'CONTENT_TYPE':self.headers['Content-Type'], }
            )           

            mt = mimetypes.guess_type(post_data["upload"].filename)[0] or "application/octet-stream"
            content = post_data["upload"].file.read()

            endpoints[self.path] = endpoint(mt,content)

            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin","*")
            self.send_header("Access-Control-Allow-Methods","*")
            self.send_header("Access-Control-Allow-Headers","*")
            self.send_header("Content-Type",mt)
            self.end_headers()
            self.wfile.write(content)
        except Exception as e:
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
