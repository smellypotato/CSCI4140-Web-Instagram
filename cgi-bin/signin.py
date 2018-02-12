#! /usr/bin/env python

import cgi
import cgitb
cgitb.enable()
print '''\
Content-type:text/html\r\n\r\n
<html>
<head>
<title>Web Instagram</title>
</head>
<body>
<h2>Web Instagram Sign in</h2>
<form action = "verifysignin.py" method= "post">
Username: <input type="text" name="username"></ br>
Password: <input type="password" name="password"></>
<input type = "submit" value = "submit">
</form>
</body>
</html>'''
