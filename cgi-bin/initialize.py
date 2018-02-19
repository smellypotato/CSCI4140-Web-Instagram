#! /usr/bin/env python

import sqlite3
import shutil

conn = sqlite3.connect('account.db')
cursor = conn.execute('''DROP TABLE IF EXISTS account''')
cursor = conn.execute('''
CREATE TABLE account (
username TEXT PRIMARY KEY,
password TEXT,
cookies TEXT,
cookieexpire TEXT);'''
)
conn.close()

conn=sqlite3.connect('image.db')
cursor = conn.execute('''DROP TABLE IF EXISTS image''')
cursor = conn.execute('''
CREATE TABLE image(
name TEXT PRIMARY KEY,
owner TEXT,
uploadtime DATETIME DEFAULT CURRENT_TIMESTAMP);'''
)
conn.close()
if os.path.exists('upload'):
    shutil.rmtree('upload')

#url = 'http://localhost:{0}/{1}'.format(8080, "cgi-bin/index.py")
url = "/cgi-bin/index.py"
print 'Content-type:text/html'
print
print '<html>'
print '<head>'
print '<title>Web Instagram</title>'
print '<META HTTP-EQUIV="Refresh" CONTENT="1;URL=%s">'%url
print '</head>'
print '<body>'
print '<p>Initialised! Returning to main page......</p>'
print '</body>'
print '</html>'''

#executable?
