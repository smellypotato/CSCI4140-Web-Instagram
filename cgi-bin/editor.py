#!/usr/bin/env python
import cgi, os
import cgitb;
import PythonMagick as pm
import imghdr
import sqlite3
import datetime
cgitb.enable()
form = cgi.FieldStorage()

img = form.getvalue("imgname")
owner = form.getvalue("owner")
conn = sqlite3.connect('image.db')
conn.execute("INSERT INTO image VALUES(?,?)",(img, owner))
conn.commit()

print 'Content-Type: text/html'
print
print '<html>'
print '<head>'
print '<title>Web Instagram</title>'
print '</head>'
print '<body>'
print '<p>', img, owner,'</p>'
cursor = conn.execute("SELECT * FROM image")
for row in cursor:
    print '<p>name: ',row[0],'</p>'
    print '<p>owner: ',row[1],'</p>'
    print '<p>time: ',row[2],'</p>'
print '</body>'
print '</html>'
