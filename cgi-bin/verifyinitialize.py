#! /usr/bin/env python
login = False
url = "/cgi-bin/index.py"
print 'Content-type:text/html'
print
print '<html>'
print '<head>'
print '<title>Web Instagram</title>'
if not login:
    print '<META HTTP-EQUIV="Refresh" CONTENT="1;URL=%s">'%url
print '</head>'
print '<body>'
if login:
    print '<form action= "initialize.py" method = "post">'
    print '<button>Please GO Ahead</button>'
    print '</form>'
    print '<form action= "index.py" method = "post">'
    print '<button>Go Back</button>'
    print '</form>'
else:
    print '<p>Admin login failed! Returning to main page......'
print '</body>'
print '</html>'
