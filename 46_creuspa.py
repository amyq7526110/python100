#!/usr/bin/env python3
import subprocess
import sys
from randpass import randpass

def adduser(username,password,fname):
    data = """user information:
%s : %s
"""
    subprocess.call('useradd %s' % username , shell=True)
    subprocess.call(

    'echo %s | passwd --stdin %s' % (password,username),
    shell=True
    )    
    with open(fname,'a') as fobj:
        fobj.write(data % (username,password))

if __name__ == '__main__':
    username = sys.argv[1]
    password = randpass()
    adduser(username,password,'/tmp/user.txt')
# 

