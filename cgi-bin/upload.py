#!/usr/bin/env python
import cgi, os
import cgitb;
import imghdr
import sqlite3
import datetime
cgitb.enable()
uploaded = False
try: #windows needs stdio set for binary mode
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY)
    msvcrt.setmode (1, os.O_BINARY)
except ImportError:
    pass
output = ""
form = cgi.FieldStorage()
owner = "public"
#nested FieldStorage instance holds the file
fileitem = form['file']
mode = form.getvalue("mode")
fn = ""
#if file is uploaded
if fileitem.filename:
    if not os.path.exists('upload'):
        os.makedirs('upload')
    #strip leading path from filename to avoid directory based attacks
    name, ext =os.path.splitext(os.path.basename(fileitem.filename))
    fn = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+ext
    output = os.path.join('upload', fn)
    open(output, 'wb').write(fileitem.file.read())
    filetype = imghdr.what(output).lower()
    fileExtension = fn.split(".")[-1].lower()
    if filetype == 'jpeg':
        filetype = 'jpg'
    #check file type match file extension
    if (filetype in ['jpg', 'gif', 'png'] and filetype == fileExtension):
        uploaded = True
        if mode == "private":
            conn = sqlite3.connect('account.db')
            httpcookie = os.environ["HTTP_COOKIE"]
            cursor = conn.execute("SELECT username FROM account where cookies = ?", (httpcookie,))
            owner = cursor.fetchone()[0]
            directory = os.path.join('upload', owner)
            if not os.path.exists(directory):
                os.makedirs(directory)
            privateoutput = os.path.join(directory,fn)
            os.rename(output, privateoutput)
            output = privateoutput

    else:
        os.remove(output)
else:
    uploaded = False
    url = 'http://localhost:{0}/{1}'.format(8080, "cgi-bin/index.py")
print 'Content-Type: text/html'
print
print '<html>'
print '<head>'
print '<title>Web Instagram</title>'
if not uploaded:
    print '<META HTTP-EQUIV="Refresh" CONTENT="1;URL=%s">'%url
print '</head>'
print '<body>'
if not uploaded:
    print '<p>Upload fail! Returning to main page......</p>'

else:
    print '<p>Uploading image......</p>'
#show the image here
    #print '<img src="%s">'%os.path.join(os.getcwd(),output)
#confirm button and go to editor.py here
    print '<form action ="editor.py" method = "post">'
    print '<input type = "hidden" value = "%s" name = "imgname">'%output
    print '<input type = "hidden" value = "%s" name = "owner">'%owner
    print '<input type = "submit" value = "Apply Filter">'
    print '</form>'

    #cancel upload
    print '<form action ="cancelupload.py" method = "post">'
    print '<input type = "hidden" value = "%s" name = "imgname">'%output
    print '<input type = "submit" value = "back">'
    print '</form>'
print '</body>'
print '</html>'
