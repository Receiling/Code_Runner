#!/usr/bin/python
# -*- coding: UTF-8 -*-

import _judger
import os
import subprocess

build_cmd = {
        "gcc"    : "sudo gcc main.c -o main -Wall -lm -O2 -std=c99 --static -DONLINE_JUDGE",
        "g++"    : "g++ main.cpp -O2 -Wall -lm --static -DONLINE_JUDGE -o main",
        "java"   : "javac Main.java",
        "ruby"   : "ruby -c main.rb",
        "perl"   : "perl -c main.pl",
        "pascal" : 'fpc main.pas -O2 -Co -Ct -Ci',
        "go"     : '/opt/golang/bin/go build -ldflags "-s -w"  main.go',
        "lua"    : 'luac -o main main.lua',
        "python2": 'python2 -m py_compile main.py',
        "python3": 'python3 -m py_compile main.py',
        "haskell": "ghc -o main main.hs",
    }
p = subprocess.Popen(build_cmd["gcc"],shell=True,cwd=os.getcwd(),stdout=subprocess.PIPE,stderr=subprocess.PIPE)   
out,err =  p.communicate()#获取编译错误信息

print "Content-type:text/html"
print
print "<html>"
print "<head>"
print "<meta charset=\"utf-8\">"
print "<title>运行结果</title>"
print "</head>"
print "<body>"

if p.returncode:
    print "<p>compile error</p>"
    print "<p>%s</p>" % (err + out)
else:
    ret = _judger.run(max_cpu_time=1000,
                  max_real_time=2000,
                  max_memory=128 * 1024 * 1024,
                  max_process_number=200,
                  max_output_size=10000,
                  max_stack=32 * 1024 * 1024,
                  # five args above can be _judger.UNLIMITED
                  exe_path="main",
                  input_path="1.in",
                  output_path="/dev/stdout",
                  error_path="/dev/stderr",
                  args=[],
                  # can be empty list
                  env=[],
                  log_path="judger.log",
                  # can be None
                  seccomp_rule_name="c_cpp",
                  uid=0,
                  gid=0)
    print "<h2>%s</h2>" % (ret)
print "</body>"
print "</html>"

