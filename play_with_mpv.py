#!/usr/bin/env python
# Plays MPV when instructed to by a chrome extension =]

import sys
from subprocess import Popen
PORT = 7531
# Use --public if you want the server and extension on different computers
hostname = 'localhost'
if '--public' in sys.argv:
    hostname = '0.0.0.0'

if sys.version_info[0] < 3:  # python 2
    import BaseHTTPServer
    import urlparse
    class CompatibilityMixin:
        def send_body(self, msg):
            self.wfile.write(msg+'\n')
            self.wfile.close()

else:  # python 3
    import http.server as BaseHTTPServer
    import urllib.parse as urlparse
    class CompatibilityMixin:
        def send_body(self, msg):
            self.wfile.write(bytes(msg+'\n', 'utf-8'))


class Handler(BaseHTTPServer.BaseHTTPRequestHandler, CompatibilityMixin):
    def respond(self, code, body=None):
        self.send_response(code)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        if body:
            self.send_body(body)

    def do_GET(self):
        try:
            url = urlparse.urlparse(self.path)
            query = urlparse.parse_qs(url.query)
        except:
            query = {}
        if query.get('mpv_args'):
            print("MPV ARGS:", query.get('mpv_args'))
        if "play_url" in query:
            urls = str(query["play_url"][0])
            #f = open("play_with_mpv.log", "a")
            #f.write("{0} \n", urls))
            #f.close()
            pipe = Popen(['mpv', urls] + query.get("mpv_args", []))
            self.respond(200, "playing...")
        else:
            self.respond(400)


def start():
    httpd = BaseHTTPServer.HTTPServer((hostname, PORT), Handler)
    print("serving on {}:{}".format(hostname, PORT))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print(" shutting down...")
        httpd.shutdown()


if __name__ == '__main__':
    start()
