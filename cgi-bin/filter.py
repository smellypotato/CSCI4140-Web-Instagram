#!/usr/bin/env python
import cgi, os
import cgitb
import subprocess
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
output = os.path.join('.', output)
cmd=""
thisimg = os.path.join('.',img)

#image = pm.Image(img)
if (filt == "border"):
    cmd = 'convert '+ thisimg + ' -bordercolor black -border 100x100 '+ output
    subprocess.Popen(cmd, shell = True)
elif (filt == "lomo"):
    cmd = 'convert ' + thisimg + ' -channel R -level 33% -channel G -level 33% ' + output
    subprocess.Popen(cmd, shell = True)
    #cmd = 'convert ..\\'+ img + ' -channel R -level 33% -channel G -level 33% ..\\'+ output
elif (filt == "lensflare"):
    cmd = 'convert lensflare.png -resize 100x ' +  os.path.join('.', 'tmp.png')
    subprocess.Popen(cmd, shell = True)
    cmd = 'composite -compose screen -gravity northwest ' +  os.path.join('.', 'tmp.png') + ' ' + thisimg + ' ' +output
    subprocess.Popen(cmd, shell = True)
elif (filt == "blackwhite"):
    cmd = 'convert ' + thisimg + ' -type grayscale ' +  os.path.join('.', 'tmp.png')
    subprocess.Popen(cmd, shell = True)
    cmd = 'convert bwgrad.png -resize 500x500\! ' +  os.path.join('.', 'bwtmp.png')
    subprocess.Popen(cmd, shell = True)
    cmd = 'composite -compose softlight -gravity center ' +  os.path.join('.', 'bwtmp.png')+ ' ' + os.path.join('.', 'tmp.png') + ' ' + output
    subprocess.Popen(cmd, shell = True)
elif (filt == "blur"):
    cmd = 'convert ' + thisimg + ' -blur 0.5x2 ' + output
    subprocess.Popen(cmd, shell = True)
#image.write(output)
url = '/cgi-bin/editor.py?imgname='+img+'&owner='+owner
print 'Content-Type: text/html'
print
print '<html>'
print '<head>'
print '<title>Web Instagram</title>'
print '<META HTTP-EQUIV="Refresh" CONTENT="3;URL=%s">'%url
print '</head>'
print '<body>'
print '<p>Applying filter......</p>'
print '<img src = %s>'%os.path.join('..','..',output)
print '</body>'
print '</html>'
