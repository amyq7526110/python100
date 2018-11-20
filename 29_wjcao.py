#!/usr/bin/env python3

import shutil 
#  文件操作的三个步骤：打开，读写，关闭

#  cp /etc/passwd /tmp

shutil.copy('/etc/passwd','/tmp')

f = open('/tmp/passwd')          #  默认读的方式打开纯文本的文件

data = f.read()                  #  read()把所有内容读出来 

print(data)

data = f.read()                  #  随着读写的进行，文件指针向后移动

# 因为第一个f.read()已经把文件指针移动到结尾了，所以再读就没有数据了

# 所以data 是空字串

f.close()

 
 
