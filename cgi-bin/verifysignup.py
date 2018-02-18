#! /usr/bin/env python

import cgi
import cgitb
import time
import os
import sqlite3
import Cookie
import random
import datetime
cgitb.enable()
cookie = ""
conn = sqlite3.connect('account.db')
form = cgi.FieldStorage()
