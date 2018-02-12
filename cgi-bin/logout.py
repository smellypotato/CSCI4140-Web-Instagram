import cgi
import cgitb
import time
import os
import sqlite3
import Cookie

cgitb.enable()
conn = sqlite3.connect('account.db')
cursor = conn.cursor()
conn.execute("UPDATE account SET cookies = null, cookieexpire = null WHERE cookies = ?", (os.environ["HTTP_COOKIE"],))
conn.commit()
cookie = Cookie.SimpleCookie()
cookie['session'] = ''
cookie['session']['expires'] = 'Thu, 01 Jan 1970 00:00:00 PST'
url = 'http://localhost:{0}/{1}'.format(8080, "cgi-bin/index.py")
print 'Content-type:text/html'
print cookie.output()
print
print '<html>'
print '<head>'
print '<title>Web Instagram</title>'
print '<META HTTP-EQUIV="Refresh" CONTENT="2;URL=%s">'%url
print '</head>'
print '<body>'
print '<p>Logging Out......</p>'
print '</body>'
print '</html>'
