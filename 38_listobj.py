#!/usr/bin/env python3


#  38-序列对象方法

from random import randint
   
alist = list()  # []
print(alist)
print(print(list('hello')))  # ['h', 'e', 'l', 'l', 'o']
astr = str()  # '' None
print(astr)
print(str(10))       # ''
print(str(['h', 'e', 'l', 'l', 'o']))  # 将列表转化成字符串
atuple = tuple()                # ()
print(atuple)
print(tuple('hello'))
num_list = [ randint(1,100) for i in range(10)]
print(num_list)
print(max(num_list))
print(min(num_list))


