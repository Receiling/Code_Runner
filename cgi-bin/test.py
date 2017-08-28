#!/usr/bin/python
# -*- coding: UTF-8 -*-
# filename:test.py

import os

print "Content-type: text/html"
print
print "<meta charset=\"utf-8\">"
#print "<p>%s<p>" % (x)
#x =  os.system("python run_oj.py")
#print x
print "Content-type: text/html"
print "<b>环境变量</b><br>";
print "<ul>"
for key in os.environ.keys():
    print "<li><span style='color:green'>%30s </span> : %s </li>" % (key,os.environ[key])
print "</ul>"
