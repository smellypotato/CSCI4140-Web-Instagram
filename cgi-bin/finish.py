#!/usr/bin/env python
import cgi, os
import cgitb
import sqlite3
#import PythonMagick as pm
import shutil
cgitb.enable()
form = cgi.FieldStorage()

img = form.getvalue("imgname")
owner = form.getvalue("owner")
filt = form.getvalue("filter")

imgdir = os.path.dirname(img)
outputdir = os.path.join(imgdir,"filter")
filteroutput =os.path.join(outputdir,os.path.basename(img))

#move temp filter image to upload
if (os.path.isfile(filteroutput)):
    if os.path.isfile(img):
        os.remove(img)
    os.rename(filteroutput, img)

#create thumbnail
imgdir = os.path.dirname(img)
tnoutputdir = os.path.join(imgdir,"thumbnail")
if not os.path.exists(tnoutputdir):
    os.makedirs(tnoutputdir)
tnoutput =os.path.join(tnoutputdir,os.path.basename(img))
#image = pm.Image(img)
#image.resize("200x200")
#image.write(tnoutput)
shutil.copy(img,tnoutput)


conn = sqlite3.connect('image.db')
conn.execute("INSERT INTO image(name ,owner) VALUES(?, ?)",(os.path.basename(img), owner))
conn.commit()
conn.close()

url = '/cgi-bin/index.py'

permalink = img
print 'Content-Type: text/html'
print
print '<html>'
print '<head>'
print '<title>Web Instagram</title>'
#print '<META HTTP-EQUIV="Refresh" CONTENT="1;URL=%s">'%url
print '</head>'
print '<body>'
print '<p>Upload Complete! <a href = "index.py">Click here to go to main page.</a></p>'
print '<p>Here is your permalink:</p>'
print '<p><a href = %s target="_blank">'%os.path.join('..',permalink) +permalink+ '</a></p>'
imgpath = os.path.join('..',img)
print '<img src = %s>'%imgpath
print '</form>'
print '</body>'
print '</html>'

#executable?
