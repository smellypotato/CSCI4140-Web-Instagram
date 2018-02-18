#! /usr/bin/env python

import cgi
import cgitb
cgitb.enable()
print '''\
Content-type:text/html\r\n\r\n
<html>
<head>
<title>Web Instagram</title>
24head>
<body>
<h2>Web Instagram Sign in</h2>
<form action = "verifysignin.py" method= "post">
Username25: <input type="text" name="username"></ br>
Password: <input type="password" name="password"></>
<input type = "submit" value = "submit">
</form>
<br>
<form action ="index.py">
<input type = "submit" value = "back">
</form>
</body>
</html>'''

#executable?
