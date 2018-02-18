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
cookie = ""

form = cgi.FieldStorage()
uid = form.getvalue("username")
pw = form.getvalue("password")
repw = form.getvalue("repassword")

fail = False
conn = sqlite3.connect('account.db')
if not fail:
    if pw != repw:
        fail = True
if not fail:
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM account WHERE username= ?", (uid,))
    count = cursor.fetchone()[0]
    if count > 0:
        fail = True
if not fail:
    expiration = datetime.datetime.now() + datetime.timedelta(days=30)
    cookie = Cookie.SimpleCookie()
    cookie["session"] = random.randint(0,1000000000)
    cookie["session"]["path"] = "/"
    cookie["session"]["expires"] = expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST")
    cookiesession,cookieexpire = cookie.output().split(';',1)
    garbage, cookiesession = cookiesession.split(':',1)
    cookiesession = cookiesession.replace(" ","")
    cursor.execute("INSERT INTO account VALUES(?,?,?,?)",(uid, pw, cookiesession, cookieexpire))
    conn.commit()
conn.close()

print 'Content-type:text/html'
if not fail:
    print cookie.output()
print
print '<html>'
print '<head>'
print '<title>Web Instagram</title>'
#print '<META HTTP-EQUIV="Refresh" CONTENT="1;URL=%s">'%url
print '</head>'
print '<body>'
print '<p>20</p>'
print '<p>%s</p>'%cookie.output()
print fail
print '</body>'
print '</html>'




'''




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
if fail:
    print '<p>Sign up failed! Retype password incorrect/Username already existed!<p>'
else: print '<p>Sign up success!<p>'
print '<p>Redirecting to main page.....</p>'
print '</body>'
print '</html>'

#executable?'''
