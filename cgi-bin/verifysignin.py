#! /usr/bin/env python

import cgi
import cgitb
import time
import os
import sqlite3
import Cookie
import random
import datetime
cgitb.enable()
login = False
conn = sqlite3.connect('account.db')
form = cgi.FieldStorage()
cookie = ""
uid = form.getvalue("username")
pw = form.getvalue("password")

cursor = conn.cursor()
cursor.execute("SELECT count(*) FROM account WHERE username= ? AND password = ?", (uid,pw))
count = cursor.fetchone()[0]

if count == 1:
    login = True
    expiration = datetime.datetime.now() + datetime.timedelta(minutes=10)
    cookie = Cookie.SimpleCookie()
    cookie["session"] = random.randint(0,1000000000)
    cookie["session"]["expires"] = expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST")
    cookiesession,cookieexpire = cookie.output().split(';',1)
    garbage, cookiesession = cookiesession.split(':',1)
    cookiesession = cookiesession.replace(" ","")
    conn.execute("UPDATE account SET cookies = ?, cookieexpire = ? WHERE username= ? AND password = ?", (cookiesession, cookieexpire, uid, pw))
    conn.commit()
#url = 'http://localhost:{0}/{1}'.format(8080, "cgi-bin/index.py")
url = "/cgi-bin/index.py"

print 'Content-type:text/html'
if login:
    print cookie.output()
print
print '<html>'
print '<head>'
print '<title>Web Instagram</title>'
print '<META HTTP-EQUIV="Refresh" CONTENT="1;URL=%s">'%url
print '</head>'
print '<body>'
if login:
    print '<p>Login Success! Redirecting to main page.....</p>'
    print cookie.output()
else:
    print '<p>Login Failed! Redirecting to main page.....</p>'
print '</html>'

#executable?
