#!/usr/bin/env python3

import os
import time


pid = os.fork()

if pid: 
    print('in parent ,sleeping...')
    print(os.waitpid(-1,1))  # 无僵尸进程可以处理，返回0
    time.sleep(20)
    print(os.waitpid(-1,1))  # 处理进程，返回子进程pid
    time.sleep(30)
    print('parent done.')
else:
    print('in chil. sleeping...')
    time.sleep(10)
    print('child done')




