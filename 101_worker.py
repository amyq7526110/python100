#!/usr/bin/env python3
import os
from time import sleep
# fork()后会出现子进程，父子进程都打印Hello World!，所以会有两行相同的内容输出。

#  print('starting...')
#  os.fork()   # 生成子进程,后续代码同时带父子进程中进行
#  print('Hello World')

 
# 可以根据fork()返回值判断是父进程，还是子进程

# print('starting....')

# pid = os.fork()  # 返回的是一个数字，对于父进程返回的是子进程的pid 子进程是0
# 
# if pid:
#     print('In parent'  )  #父进程执行后
# else:
#     print('in child')     #子进程执行后
# 
# print('\033[32mDone\033[0m')  # 父子都会执行

for i in range(5):
    pid = os.fork()   #父进程的工作是生成子进程
    if not pid:
        print('hello')
        sleep(10)
#        exit()   # 注释这一行 查看结果





