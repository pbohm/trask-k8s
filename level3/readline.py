#!/usr/bin/python3
import http.server
import socketserver
import random,sys
from urllib.parse import urlparse
from urllib.parse import parse_qs

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Sending an '200 OK' response
        self.send_response(200)

        # Setting the header
        self.send_header("Content-type", "text/text")

        # Whenever using 'send_header', you also have to call 'end_headers'
        self.end_headers()

        name = 'HTTP reader'
        query_components = parse_qs(urlparse(self.path).query)
        if 'name' in query_components:
            name = query_components["name"][0]

        lines = open("filetoranderize").readlines()
        msg = lines[random.randrange(len(lines))]

        self.wfile.write(bytes(msg, "utf8"))

        return

# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 8080
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()
