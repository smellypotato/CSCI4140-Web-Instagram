#! /usr/bin/env python

import cgi
import cgitb
import time
import os
import sqlite3
import Cookie

cgitb.enable()
conn = sqlite3.connect('account.db')
form = cgi.FieldStorage()

fail = False
httpcookie = os.environ["HTTP_COOKIE"]
cursor = conn.execute("SELECT username FROM account where cookies = ?", (httpcookie,))
uid = cursor.fetchone()[0]
oldpw = form.getvalue("oldpassword")
newpw = form.getvalue("newpassword")
renewpw = form.getvalue("renewpassword")

if not fail:
    if newpw != renewpw:
        fail = True
if not fail:
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM account WHERE username= ? AND password = ?", (uid,oldpw))
    if cursor.fetchone()[0] != 1:
        fail = True
if not fail:
    conn.execute("UPDATE account SET password = ? WHERE username= ? AND password = ?", (newpw, uid, oldpw))
    conn.commit()

url = 'http://localhost:{0}/{1}'.format(8080, "cgi-bin/index.py")
print 'Content-type:text/html'
print
print '<html>'
print '<head>'
print '<title>Web Instagram</title>'
print '<META HTTP-EQUIV="Refresh" CONTENT="1;URL=%s">'%url
print '</head>'
print '<body>'
if fail:
    print '<p>Update Failed! Redirecting to main page.....<p>'
else: print '<p>Update success! Redirecting to main page.....<p>'
print '</body>'
print '</html>'
