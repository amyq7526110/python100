#!/usr/bin/env python3

#  1、设置一个用于随机取出字符的基础字符串，本例使用大小写字母加数字
#  2、循环n次，每次随机取出一个字符
#  3、将各个字符拼接起来，保存到变量result中

from random import choice

import string 

all_chs =  string.ascii_letters + string.digits + '_'  # 大小写加数字和下划线

def gen_pass(n=8):
    result = [ choice(all_chs) for i in range(n)  ] 
    return ''.join(result)

if __name__ == '__main__':
   print(gen_pass())
   print(gen_pass(4))
   print(gen_pass(10))


    


