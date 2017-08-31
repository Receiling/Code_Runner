#!/usr/bin/python
# -*- coding: UTF-8 -*-

import _judger
import subprocess
import os
# CGI处理模块
import cgi, cgitb

form = cgi.FieldStorage() 

# 获取数据
site_id = form.getvalue('id')
site_code  = form.getvalue('code')

cpp_file = open("main.c", "w+b")
cpp_file.write(site_code)
cpp_file.close()

build_cmd = {
        "gcc"    : "sudo gcc main.c -o main -Wall -lm -O2 -std=c99 --static -DONLINE_JUDGE",
        "g++"    : "g++ main.cpp -O2 -Wall -lm --static -DONLINE_JUDGE -o main",
        "java"   : "javac Main.java",
        "ruby"   : "ruby -c main.rb",
        "perl"   : "perl -c main.pl",
        "pascal" : 'fpc main.pas -O2 -Co -Ct -Ci',
        "go"     : '/opt/golang/bin/go build -ldflags "-s -w"  main.go',
        "lua"    : 'luac -o main main.lua',
        "python": 'sudo python run.py main.c out.txt gcc',
        "python3": 'python3 -m py_compile main.py',
        "haskell": "ghc -o main main.hs",
    }
p = subprocess.Popen(build_cmd["python"],shell=True,cwd=os.getcwd(),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err =  p.communicate()#获取编译错误信息

print "Content-type:text/html"
print
print "<html>"
print "<head>"
print "<meta charset=\"utf-8\">"
print "<title>运行结果</title>"
print "</head>"
print "<body>"

ret = p.stdout.readline()  
if ret == "compile error":
    print "<p>compile error</p>"
else:
    print "<h2>run_conformation: %s</h2>" % (ret)
    output_file = open("out.txt", "r")
    output = output_file.read()
    output_file.close()
    print "<h2>output: %s</h2>" % (output)
print "</body>"
print "</html>"
