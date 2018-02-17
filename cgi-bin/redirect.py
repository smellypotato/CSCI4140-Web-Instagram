#! /usr/bin/env python
import cgi
import cgitb
import Cookie
import sqlite3
conn = sqlite3.connect('account.db')
cursor = conn.cursor()
conn.execute("UPDATE account SET cookies = null, cookieexpire = null WHERE cookies IS NOT null")
conn.commit()

cookie = Cookie.SimpleCookie()
cookie['session'] = ''
cookie['session']['expires'] = 'Thu, 01 Jan 1970 00:00:00 PST'

#url = 'http://localhost:{0}/{1}'.format(8080, "cgi-bin/index.py")
url = "index.py"
print 'Content-type:text/html'
print cookie.output()
print
print '<html>'
print '<head>'
print '<title>Web Instagram</title>'
print '<META HTTP-EQUIV="Refresh" CONTENT=0;URL="%s">'%url
print '</head>'
print '<body>'
print '<p>Redirecting......hi!</p>'
print '<form action= "/cgi-bin/index.py" method = "post">'
print '<button>main page</button>'
print '</form>'
print '</body>'
print '</html>'

#executable?
