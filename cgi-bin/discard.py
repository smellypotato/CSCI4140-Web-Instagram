import cgi, os
import cgitb;

cgitb.enable()
form = cgi.FieldStorage()

imgname = form.getvalue("imgname")
owner = form.getvalue("owner")

imgdir = os.path.dirname(imgname)
outputdir = os.path.join(imgdir,"filter")
filterimg =os.path.join(outputdir,os.path.basename(imgname))

#remove related image
if os.path.isfile(filterimg):
    os.remove(filterimg)
if os.path.isfile(imgname):
    os.remove(imgname)

url = 'http://localhost:{0}/{1}'.format(8080, "cgi-bin/index.py")
print 'Content-Type: text/html'
print
print '<html>'
print '<head>'
print '<title>Web Instagram</title>'
print '<META HTTP-EQUIV="Refresh" CONTENT="1;URL=%s">'%url
print '</head>'
print '<body>'
print '<p>Discarding Image......</p>'
print '</form>'
print '</body>'
print '</html>'
