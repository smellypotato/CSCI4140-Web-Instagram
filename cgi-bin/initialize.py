#! /usr/bin/env python

import sqlite3

conn = sqlite3.connect('account.db')
cursor = conn.execute('''DROP TABLE IF EXISTS account''')
cursor = conn.execute('''
CREATE TABLE account (
username TEXT PRIMARY KEY,
password TEXT,
cookies TEXT,
cookieexpire TEXT);'''
)
url = 'http://localhost:{0}/{1}'.format(8080, "cgi-bin/index.py")
print 'Content-type:text/html'
print
print '<html>'
print '<head>'
print '<title>Web Instagram</title>'
print '<META HTTP-EQUIV="Refresh" CONTENT="2;URL=%s">'%url
print '</head>'
print '<body>'
print '<p>Initialised! Returning to main page......</p>'
print '</body>'
print '</html>'''
conn.close()
