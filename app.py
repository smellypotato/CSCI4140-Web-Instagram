#! /usr/bin/env python

# https://pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-1/
# https://docs.python.org/2/library/basehttpserver.html
# https://docs.python.org/2/library/cgihttpserver.html

import BaseHTTPServer
import CGIHTTPServer
import webbrowser

PORT = 8080
#TODO: check that port is available,
# and look for a different one if it isn't.
#script_path = "cgi-bin/redirect.py"

server_class = BaseHTTPServer.HTTPServer
handler_class = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", PORT)
handler_class.cgi_directories = ["/cgi-bin"]

#url = 'http://localhost:{0}/{1}'.format(PORT, script_path)
#webbrowser.open_new_tab(url)
httpd = server_class(server_address, handler_class)

httpd.serve_forever()
