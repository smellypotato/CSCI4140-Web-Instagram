#! /usr/bin/env python

import cgi
import cgitb
import time
import os
import sqlite3
import Cookie
import math
cgitb.enable()
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

print "Content-type:text/html"
if login:
    try:
        cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
        print "session = " + cookie["session"].value,'\r\n'
    except (Cookie.CookieError, KeyError):
        print None
else:
    print cookie.output() ,'\r\n'
print
conn.close()
print "<html>"
print "<head>"
print "<title>Web Instagram</title>"
print "</head>"

print '<style>'
print '.pagination {'
print '     display: inline-block;'
print '}'
print '.pagination a {'
print '    color: black;'
print '    float: left;'
print '    padding: 8px 16px;'
print '    text-decoration: none;'
print '}'
print '.pagination a.active {'
print '    background-color: #4CAF50;'
print '    color: white;'
print '}'
print '.pagination a:hover:not(.active) {background-color: #ddd;}'
print '</style>'
print '<body>'
print '<h2>Welcome to web instagram by Potato</h2>'
print 'hi,', user
print '</body>'
print '</html>'
'''


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
#image db info
cursor = conn.execute("SELECT count(*) FROM image WHERE owner = 'public' OR owner = ?", (user,))
imgno = cursor.fetchone()[0]
pageno = imgno/8 + (imgno % 8 > 0)
form = cgi.FieldStorage()
currentpage = form.getvalue("page")
if currentpage == None:
    currentpage = 1
else:
    currentpage = int(currentpage)
#page numbers
#print imgno, pageno, currentpage
print '<div class=".pagination">'
if currentpage != 1:
    print '  <a href="/cgi-bin/index.py?page=%s">&laquo;</a>'%str(currentpage - 1)
for i in range(1, pageno + 1):
    active = ""
    if currentpage == i:
        active = 'class="active" '
    print '  <a '+active+'href="/cgi-bin/index.py?page='+str(i)+'">'+str(i)+'</a>'
if currentpage != pageno and pageno != 0:
    print '  <a href="/cgi-bin/index.py?page=%s">&raquo;</a>'%str(currentpage + 1)
print '</div>'
print '<br>'
offset = (currentpage-1)*8
#display image
cursor = conn.execute("SELECT * FROM image WHERE owner = 'public' OR owner = ? ORDER BY uploadtime DESC LIMIT 8 OFFSET ?", (user, offset))
for row in cursor:
    if (row[1] == "public"):
        permalink = os.path.join('..','upload','thumbnail',row[0])
        original = os.path.join('..','upload',row[0])
    else:
        permalink = os.path.join('..','upload',row[1],'thumbnail',row[0])
        original = os.path.join('..','upload',row[1],row[0])
    print '<a target = "_blank" href = "%s"><img src = %s></a>'%(original,permalink)

conn.close()

#executable?'''
