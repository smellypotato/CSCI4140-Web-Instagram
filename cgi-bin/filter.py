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
    cmd = 'convert lensflare.png -resize 200x200 tmp.png'
    subprocess.Popen(cmd, shell = True)
    cmd = 'composite -compose screen -gravity northwest tmp.png ' + thisimg + ' ' +output
    subprocess.Popen(cmd, shell = True)
    #flare = pm.Image("lensflare.png")
    #geo =str(image.size().width())+'x'+str(image.size().height())+'!'
    #flare.resize(geo)#+str(image.size().height()))
    #image.composite(flare,pm.GravityType.NorthWestGravity,pm.CompositeOperator.ScreenCompositeOp)
#elif (filt == "blackwhite"):
    #cmd =
    #image.colorSpace(pm.ColorspaceType.GRAYColorspace)
    #if not image.monochrome():
    #    image.monochrome(True)
    #bw = pm.Image("bwgrad.png")
    #geo =str(image.size().width())+'x'+str(image.size().height())+'!'
    #bw.resize(geo)
    #image.composite(bw,pm.GravityType.CenterGravity,pm.CompositeOperator.SoftLightCompositeOp)
elif (filt == "blur"):
    cmd = 'convert ' + thisimg + '-blur 0.5x2 ' + output
    subprocess.Popen(cmd, shell = True)
    #image.blur(5,5)
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
print '<img src = %s>'%output#os.path.join('..',output)
print '</body>'
print '</html>'
