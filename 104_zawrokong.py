#!/usr/bin/env python3
import os 

import time

pid = os.fork()

if pid: 
    print('In parent , sleeping... ')
    time.sleep(30)
    print('parent done.')
else:
    print('In child .sleeping...')
    time.sleep(10)
    print('child done')  # 10秒后 子进程变成了僵尸进程

# watch -n1 ps a  当子进程成为僵尸进程时，显示为Z
# kill 试图杀死僵尸进程、父进进程，查看结果
    
