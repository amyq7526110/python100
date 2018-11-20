#!/usr/bin/env python3

from random import randint

def func(x):
    return x * 2 + 1

if __name__ == '__main__':
    alist = [randint(1,100) for i in range(10) ]
    print(alist)
    # map将第二个参数中的每一项交给func函数进行加工，保留加工后的结果
    result  = map(func,alist)  # 使用常规函数
    result2 = map(lambda x: x * 2 +1,alist)  #  使用匿名函数
    print(result)                            #  map返回一个对象   
    print(list(result))
    print(list(result2))
