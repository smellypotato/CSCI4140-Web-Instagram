#!/usr/bin/env python
import cgi, os
import cgitb;

cgitb.enable()
form = cgi.FieldStorage()

imgname = form.getvalue("imgname")
owner = form.getvalue("owner")

imgdir = os.path.dirname(imgname)
outputdir = os.path.join(imgdir,"filter")
filterimg =os.path.join(outputdir,os.path.basename(imgname))

#replace filtered image with orginal image
img = imgname
os.remove(filterimg)
os.rename(img, filterimg)

url = '/cgi-bin/editor.py?imgname='+imgname+'&owner='+owner

print 'Content-Type: text/html'
print
print '<html>'
print '<head>'
print '<title>Web Instagram</title>'
print '<META HTTP-EQUIV="Refresh" CONTENT="1;URL=%s">'%url
print '</head>'
print '<body>'
print '<p>Undo......</p>'
#print '<img src = %s>'%displayimg
print '<form action ="editor.py" method = "post">'
print '<input type = "hidden" value = "%s" name = "imgname">'%imgname
print '<input type = "hidden" value = "%s" name = "owner">'%owner
print '<input type = "submit" value = "Apply Filter">'
print '</form>'
print '</body>'
print '</html>'
