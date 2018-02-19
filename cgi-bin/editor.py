#!/usr/bin/env python
import cgi, os
import cgitb;
import imghdr
import sqlite3
import datetime
cgitb.enable()
form = cgi.FieldStorage()

imgname = form.getvalue("imgname")
owner = form.getvalue("owner")

imgdir = os.path.dirname(imgname)
outputdir = os.path.join(imgdir,"filter")
filteroutput =os.path.join(outputdir,os.path.basename(imgname))
if (os.path.isfile(filteroutput)):
    img = filteroutput
else:
    img = imgname
displayimg = os.path.join('..',img)

undo = ""
if not os.path.isfile(imgname) or not os.path.isfile(filteroutput):
    undo = "disabled"

print 'Content-Type: text/html'
print
print '<html>'
print '<head>'
print '<title>Web Instagram</title>'
print '</head>'
print '<body>'
print '<h2>Editor</h2>'
print '<img src = %s>'%displayimg

print '<form action ="filter.py" method = "post">'
print '<p>'
print '<input type="radio" name="filter" value = "border" checked>Border'
print '<input type="radio" name="filter" value = "lomo">Lomo'
print '<input type="radio" name="filter" value = "lensflare">Lens Flare'
print '<input type="radio" name="filter" value = "blackwhite">Black & White'
print '<input type="radio" name="filter" value = "blur">Blur'
print '<input type="radio" name="filter" value = "fake">fake'
print '</p>'
print '<input type = "hidden" value = "%s" name = "imgname">'%imgname
print '<input type = "hidden" value = "%s" name = "owner">'%owner
print '<input type = "submit" value = "Apply Filter">'
print '</form>'

print '<form action ="undo.py" method = "post">'
print '<input type = "hidden" value = "%s" name = "imgname">'%imgname
print '<input type = "hidden" value = "%s" name = "owner">'%owner
print '<input type = "submit" value = "Undo" ' + undo +'>'
print '</form>'

print '<form action ="finish.py" method = "post">'
print '<input type = "hidden" value = "%s" name = "imgname">'%imgname
print '<input type = "hidden" value = "%s" name = "owner">'%owner
print '<input type = "submit" value = "Finish" >'
print '</form>'

print '<form action ="discard.py" method = "post">'
print '<input type = "hidden" value = "%s" name = "imgname">'%imgname
print '<input type = "hidden" value = "%s" name = "owner">'%owner
print '<input type = "submit" value = "Discard" >'
print '</form>'

#debug
conn = sqlite3.connect('image.db')

cursor = conn.execute("SELECT * FROM image ORDER BY uploadtime DESC")
for row in cursor:
    print '<p>name: ',row[0],'</p>'
    print '<p>owner: ',row[1],'</p>'
    print '<p>time: ',row[2],'</p>'
conn.close()
print '</body>'
print '</html>'

#executable?
