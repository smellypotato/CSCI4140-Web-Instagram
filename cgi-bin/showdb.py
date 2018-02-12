#! /usr/bin/env python

import cgi
import cgitb
import time
import os
import sqlite3
import Cookie
cgitb.enable()
conn = sqlite3.connect('account.db')
url = 'http://localhost:{0}/{1}'.format(8080, "cgi-bin/index.py")
print 'Content-type:text/html'
try:
    cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
    print "session = " + cookie["session"].value + '\n'
except (Cookie.CookieError, KeyError):
    print None
print
print '<html>'
print '<head>'
print '<title>Web Instagram</title>'
print '</head>'
print '<body>'
print '<h2>Show DB</h2>'
cursor = conn.execute("SELECT * FROM account")
for row in cursor:
    print '<p>Username: ',row[0],'</p>'
    print '<p>Password: ',row[1],'</p>'
    print '<p>Cookie: ',row[2],'</p>'
    print '<p>Cookieexpire: ',row[3],'</p>'
print '<p>OS cookie:',os.environ["HTTP_COOKIE"],'</p>'
print '</body>'
print '</html>'

conn.close()
