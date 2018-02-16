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
<h2>Web Instagram Update Account</h2>
<form action = "verifyupdate.py" method= "post">
Original Password: <input type="password" name="oldpassword"></ br>
New Password: <input type="password" name="newpassword"></ br>
Retype New Password: <input type="password" name="renewpassword"></>
<input type = "submit" value = "submit">
</form>
<br>
<form action ="index.py">
<input type = "submit" value = "back">
</form>'
</body>
</html>'''
