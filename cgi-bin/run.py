#!/usr/bin/python
# -*- coding: UTF-8 -*-

import _judger
import os
import sys

#python main.py input_file output_file language(gcc/g++/java)
input_file = sys.argv[1]
ss = input_file.split('.', 2)
exe_file = ss[0]
output_file = sys.argv[2]
language = sys.argv[3]
language_map = {
    "gcc"  : "gcc",
    "g++"  : "g++",
    "java" : "javac",
}

if language == "java":
    cmd = language_map[language] + " " + input_file
else:
    cmd = language_map[language] + " " + input_file + " -o " + exe_file

if os.system(cmd):
    print("compile error")
    exit(1)

ret = _judger.run(max_cpu_time=1000,
                  max_real_time=2000,
                  max_memory= 1024 * 1024 * 1024,
                  max_process_number=200,
                  max_output_size=10000,
                  max_stack=32 * 1024 * 1024,
                  # five args above can be _judger.UNLIMITED
                  exe_path=exe_file,
                  input_path="/dev/null",
                  #can not be empty
                  output_path=output_file,
                  error_path="error.log",
                  args=[],
                  # can be empty list
                  env=[],
                  log_path="judger.log",
                  # can be None
                  seccomp_rule_name="c_cpp",
                  uid=0,
                  gid=0)
print(ret)
