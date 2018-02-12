#!/usr/bin/env python
import cgi, os
import cgitb;
import PythonMagick as pm
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

form = cgi.FieldStorage()

#nested FieldStorage instance holds the file
fileitem = form['file']
mode = form.getvalue("mode")
fn = ""
#if file is uploaded
if fileitem.filename:
    #strip leading path from filename to avoid directory based attacks
    fn = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+os.path.splitext(os.path.basename(fileitem.filename))[1]
    output = os.path.join(os.path.os.getcwd() + '\upload', fn)
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
            user = cursor.fetchone()[0]
            directory = os.path.join(os.path.os.getcwd() + '\upload', user)
            if not os.path.exists(directory):
                os.makedirs(directory)
            privateoutput = os.path.join(directory,fn)
            os.rename(output, privateoutput)

    else:
        os.remove(output)
else:
    uploaded = False
if uploaded:
    message = 'The file ' + fn + ' was uploaded to ' + mode +' directory successfully!'
else:
    message = 'No file was uploaded!'

url = 'http://localhost:{0}/{1}'.format(8080, "cgi-bin/index.py")
print 'Content-Type: text/html\n'
print '<html>'
print '<head>'
print '<title>Web Instagram</title>'
print '<META HTTP-EQUIV="Refresh" CONTENT="1;URL=%s">'%url
print '</head>'
print '<body>'
print '<p>'+fn+'</p>'
print '</body>'
print '</html>'
