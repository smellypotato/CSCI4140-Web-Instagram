#!/usr/bin/env python
import cgi, os
import cgitb
import subprocess
#import re
#import PythonMagick as pm

cgitb.enable()
form = cgi.FieldStorage()

img = form.getvalue("imgname")
owner = form.getvalue("owner")
filt = form.getvalue("filter")

imgdir = os.path.dirname(img)
outputdir = os.path.join(imgdir,"filter")
if not os.path.exists(outputdir):
    os.makedirs(outputdir)
output =os.path.join(outputdir,os.path.basename(img))
#replace orginal image with filtered image
if (os.path.isfile(output)):
    if os.path.isfile(img):
        os.remove(img)
    os.rename(output, img)
cmd=""
thisimg = os.path.join('..',img)
#image = pm.Image(img)

    #image.blur(5,5)
#image.write(output)
#url = 'http://localhost:{0}/{1}'.format(8080, "cgi-bin/editor.py")
url = '/cgi-bin/editor.py?imgname='+img+'&owner='+owner
print 'Content-Type: text/html'
print
print '<html>'
print '<head>'
print '<title>Web Instagram</title>'
print '<META HTTP-EQUIV="Refresh" CONTENT="3;URL=%s">'%url
print '</head>'
print '<body>'
print '<p>Applying filter......%s %s %s</p>'%(img, thisimg, output)
#print '<img src = %s>'%os.path.join('..',output)
#print '<form action ="editor.py" method = "post">'
#print '<input type = "hidden" value = "%s" name = "imgname">'%img
#print '<input type = "hidden" value = "%s" name = "owner">'%owner
#print '<input type = "submit" value = "Apply Filter">'
#print '</form>'
print '</body>'
print '</html>'

#executable?
