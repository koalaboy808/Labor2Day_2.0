#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('app.db')

print "Opened database successfully";

cursor = conn.execute("SELECT username, _password  from Employers")
for row in cursor:
   print "USERNAME = ", row[0]
   print "PASSWORD = ", row[1], "\n"

cursor2 = conn.execute("SELECT request_title, emp_id  from employer_request")
for row in cursor2:
   print "REQUEST TITLE = ", row[0]
   print "ASSOCIATED EMPLOYER = ", row[1], "\n"

cursor3 = conn.execute("SELECT laborer_first_name  from laborer")
for row in cursor3:
   print "NAME = ", row[0], "\n"

print "Operation done successfully";
conn.close()