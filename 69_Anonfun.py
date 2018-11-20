#!/usr/bin/env python3
from random import randint 

def func1(x):
    return x % 2

if __name__ == '__main__':
    alist = [ randint(1,100)  for i in range(10) ]
    print(alist)
    # filter要求第一个参数是函数，该函数必须返回True或False
    # 执行时把alist的每一项作为 func1的参数，返回真留下，否则过滤掉
    # filter函数的参数又是函数，称作高阶函数
    result = filter(func1,alist)  # 不使用匿名函数
    print(list(result))
    result2  = filter(lambda x : x % 2, alist) # 匿名函数
    print(list(result2))
   
#   [15, 78, 12, 38, 30, 33, 96, 45, 53, 58]
#   [15, 33, 45, 53]
#   [15, 33, 45, 53]



