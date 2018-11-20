#!/usr/bin/env python3

import getpass   # 导入模块

username = input('username: ')

# getpass 模块中。有一个方法叫做getpass

password = getpass.getpass('password: ')

if username == 'bob' and password == '123456':
    print('Login successful')
else:
    print('Login incorrect')
   

