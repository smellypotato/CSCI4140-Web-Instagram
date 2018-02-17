#!/usr/bin/env python
import cgi, os
import cgitb;

form = cgi.FieldStorage()

img = form.getvalue("imgname")
os.remove(img)

url = 'http://localhost:{0}/{1}'.format(8080, "cgi-bin/index.py")
print 'Content-type:text/html'
print ''
print '<html>'
print '<head>'
print '<title>Web Instagram</title>'
print '<META HTTP-EQUIV="Refresh" CONTENT="1;URL=%s">'%url
print '</head>'
print '<body>'
print '<p>Cancelling upload image......</p>'
print '<p>' + img + '</p>'
print '</body>'
print '</html>'

#executable?
