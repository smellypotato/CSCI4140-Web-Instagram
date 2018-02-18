#! /usr/bin/env python

import cgi
import cgitb
cgitb.enable()

print "Content-type:text/html\r\n\r\n"
print '''
<html>
<head>
<title>Web Instagram</title>
</head>
<body>
<h2>Web Instagram Sign Up</h2>
<form action = "verifysignup.py" method= "post">
Username26: <input type="text" name="username"></ br>
Password: <input type="password" name="password"></ br>
Retype Password: <input type="password" name="repassword"></>
<input type = "submit" value = "submit">
</form>
<br>
<form action ="index.py">
<input type = "submit" value = "back">
</form>
</body>
</html>'''

#executable?
