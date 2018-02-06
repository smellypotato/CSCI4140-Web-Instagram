import cgi
import cgitb
import time
import os

header = "Content-type: text/html\r\n\r\n"

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Hello World</title>
</head>
<body>
  <h2>Hello World!</h2>
  <p>Finally can see you!</p>
</body>
</html>
"""

print header + html
