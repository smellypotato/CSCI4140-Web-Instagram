#!/usr/bin/env python
import cgi, os
import cgitb
import subprocess
import re
import PythonMagick as pm

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

image = pm.Image(img)
if (filt == "border"):
    #cmd = 'convert '+ img + ' -bordercolor Black -border 100x100 '+ output
    image.borderColor("Black")
    image.border("50x50")
#elif (filt == "lomo"):
    #image.channel(pm.ChannelType.RedChannel)
elif (filt == "lensflare"):
    flare = pm.Image("lensflare.png")
    flare.resize(str(image.size().width())+'x')#+str(image.size().height()))
    image.composite(flare,pm.GravityType.NorthWestGravity,pm.CompositeOperator.ScreenCompositeOp)
elif (filt == "blackwhite"):
    image.colorSpace(pm.ColorspaceType.GRAYColorspace)
    bw = pm.Image("bwgrad.png")
    bw.resize(str(image.size().width())+'x'+str(image.size().height()))
    image.composite(bw,pm.GravityType.CenterGravity,pm.CompositeOperator.SoftLightCompositeOp)

elif (filt == "blur"):
    image.blur(1,1)
image.write(output)
#subprocess.Popen(cmd, shell=True)

#url = 'http://localhost:{0}/{1}'.format(8080, "cgi-bin/editor.py")
print 'Content-Type: text/html'
print
print '<html>'
print '<head>'
print '<title>Web Instagram</title>'
#print '<META HTTP-EQUIV="Refresh" CONTENT="1;URL=%s">'%url
print '</head>'
print '<body>'
print '<p>Applying filter......</p>'
print '<p>' + img + '</p>'
print '<form action ="editor.py" method = "post">'
print '<input type = "hidden" value = "%s" name = "imgname">'%img
print '<input type = "hidden" value = "%s" name = "owner">'%owner
print '<input type = "submit" value = "Apply Filter">'
print '</form>'
print '</body>'
print '</html>'
