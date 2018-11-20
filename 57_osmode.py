#!/usr/bin/env python3

import os 

os.getcwd()             # pwd
os.listdir()            # ls -a
os.listdir('/tmp')      # ls -a /tmp
os.mkdir('/tmp/mydemo') # mkdir /tmp/mydemo
os.chdir('/tmp/mydemo') # cd /tmp/mydemo
os.listdir()  
os.mknod('test.txt')    # touch test.txt
os.symlink('/etc/hosts','zhuji')  # ln -s /etc/hosts zhuji
os.path.isfile('test.txt')        #  [ -f test.txt ]
os.path.islink('zhuji')           #  [ -i zhuji    ]
os.path.isdir('/etc')             #  [ -d /etc     ]
os.path.exists('/tmp')            #  [ -e /tmp     ]
os.path.basename('/tmp/abc/aaa.txt')   #  basename $0  aaa.txt
os.path.basename('/tmp/abc/aaa.txt')   #  dirname $0   /tmp/abc
os.path.split('/tmp/abc/aaa.txt')      # 
os.path.join('/home/tom','xyz.txt')    # /home/tom/xyz.txt
os.path.abspath('test.txt')            # 返回当前目录test.txt的绝对路径







