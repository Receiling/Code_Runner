#!/usr/bin/python
# -*- coding: UTF-8 -*-

import _judger

def run(exe_file, input_file, output_file, error_file,  language):  

    ret = _judger.run(max_cpu_time=1000,
                  max_real_time=2000,
                  max_memory=128 * 1024 * 1024,
                  max_process_number=200,
                  max_output_size=10000,
                  max_stack=32 * 1024 * 1024,
                  # five args above can be _judger.UNLIMITED
                  exe_path= exe_file,
                  input_path= input_file,
                  output_path=output_file,
                  error_path=error_file,
                  args=[],
                  # can be empty list
                  env=[],
                  log_path="judger_log/judger.log",
                  # can be None
                  seccomp_rule_name=language,
                  uid=0,
                  gid=0)
    return ret

