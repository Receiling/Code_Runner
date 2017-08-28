#!/usr/bin/python
# -*- coding: UTF-8 -*-

import _judger
import os

def run(code_id):
  
    if os.system("gcc main.c -o main"):
        print("compile error")
        return 0

    ret = _judger.run(max_cpu_time=1000,
                  max_real_time=2000,
                  max_memory=128 * 1024 * 1024,
                  max_process_number=200,
                  max_output_size=10000,
                  max_stack=32 * 1024 * 1024,
                  # five args above can be _judger.UNLIMITED
                  exe_path= "main",
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
    return ret

print run(1)

