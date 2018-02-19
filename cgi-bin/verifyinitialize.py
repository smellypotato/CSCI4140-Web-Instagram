#! /usr/bin/env python
import cgi
import cgitb
import time
import os
import sqlite3

form = cgi.FieldStorage()
uid = form.getvalue("username")
pw = form.getvalue("password")
newpw = form.getvalue("newpassword")

login == False

conn = sqlite3.connect('admin.db')
cursor = conn.cursor()
cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='admin';")
if cursor.fetchone()[0] == 0 and uid == "admin" and pw == "admin":
    login = True
    cursor = conn.execute('''
    CREATE TABLE admin(
    name TEXT PRIMARY KEY,
    password TEXT'''
    )
    cursor = conn.execute('INSERT INTO admin VALUES(?,?)',(uid,pw))
    conn.commit()
else:
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM admin WHERE username= ? AND password = ?", (uid,pw))
    if cursor.fetchone()[0] == 1:
        login = True
        conn.execute("UPDATE account SET password = ? WHERE username= ? AND password = ?", (newpw, uid, pw))
        conn.commit()

url = "/cgi-bin/index.py"
print 'Content-type:text/html'
print
print '<html>'
print '<head>'
print '<title>Web Instagram</title>'
if not login:
    print '<META HTTP-EQUIV="Refresh" CONTENT="1;URL=%s">'%url
print '</head>'
print '<body>'
if login:
    print '<form action= "initialize.py" method = "post">'
    print '<button>Please GO Ahead</button>'
    print '</form>'
    print '<form action= "index.py" method = "post">'
    print '<button>Go Back</button>'
    print '</form>'
else:
    print '<p>Admin login failed! Returning to main page......'
print '</body>'
print '</html>'
