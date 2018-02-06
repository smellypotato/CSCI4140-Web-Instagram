import cgi
import cgitb
import time
import os
cgitb.enable()

header = "Content-type: text/html\r\n\r\n"


date_string = time.strftime('%A, %B %d, %Y at %I:%M:%S %p %Z')

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Hello World</title>
</head>
<body>
  <h2>Hello World!</h2>
  <p>Fianlly see you!</p>
</body>
</html>
"""
print header + html
