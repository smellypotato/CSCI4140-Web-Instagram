#! /usr/bin/env python

import cgi
import cgitb
import time
import os
import sqlite3
import Cookie
cookie = ""
cgitb.enable()
login = False
user = "guest"
conn = sqlite3.connect('account.db')
httpcookie = os.environ["HTTP_COOKIE"]
cursor = conn.execute("SELECT count(*), username FROM account where cookies = ?", (httpcookie,))
row = cursor.fetchone()
if (row[0] != 0):
    user = row[1]
    login = True
if not login:
    cookie = Cookie.SimpleCookie()
    cookie['session'] = ''
    cookie['session']['expires'] = 'Thu, 01 Jan 1970 00:00:00 PST'
print 'Content-type:text/html'
if login:
    try:
        cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
        print "session = " + cookie["session"].value
    except (Cookie.CookieError, KeyError):
        print None
else:
    print cookie.output
conn.close()
#use bootstrap to show image
print "<!DOCTYPE>"
print ""
print '<html>'
print '<head>'
print '<title>Web Instagram</title>'
print '</head>'
print '<body>'
print '<h2>Welcome to web instagram by Potato</h2>'
print 'hi,', user
if login:
    print '<p>Account Management</p>'
    print '<form action= "updateaccount.py" method = "post">'
    print '<button>Update Account</button>'
    print '</form>'
    print '<form action= "logout.py" method = "post">'
    print '<button>Log Out</button>'
    print '</form>'
    print '<br>'
    print '<p>Upload Photo</p>'
    print '<form enctype="multipart/form-data" action= "upload.py" method="post">'
    print '<p>File: <input type="file" name="file" accept="image/gif, image/jpeg, image/png"></p>'
    print '<p>'
    print '<input type="radio" name="mode" value = "public" checked>public'
    print '<input type="radio" name="mode" value = "private">private'
    print '</p>'
    print '<p><input type="submit" value="Upload Photo"></p>'
    print '</form>'
else:
    print '<form action= "signin.py" method = "post">'
    print '<button>Sign In</button>'
    print '</form>'
    print '<form action= "signup.py" method = "post">'
    print '<button>Sign Up</button>'
    print '</form>'
print '<form action= "/cgi-bin/initialize.py" method = "post">'
print '<button>Initialize Account DB</button>'
print '</form>'
print '<form action= "/cgi-bin/showdb.py" method = "post">'
print '<button>Show DB</button>'
print '</form>'
conn = sqlite3.connect("image.db")
cursor = conn.execute("SELECT * FROM image WHERE owner = 'public' OR owner = ? ORDER BY uploadtime DESC", (user,))
for row in cursor:
    if (row[1] == "public"):
        permalink = os.path.join('..','upload','thumbnail',row[0])
        original = os.path.join('..','upload',row[0])
    else:
        permalink = os.path.join('..','upload',row[1],'thumbnail',row[0])
        original = os.path.join('..','upload',row[1],row[0])
    print '<a target = "_blank" href = "%s"><img src = %s></a>'%(original,permalink)
print '</body>'
print '</html>'
conn.close()
