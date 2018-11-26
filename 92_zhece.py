#!/usr/bin/env python3
import re

m = re.match('f..','food')       # 匹配到返回对象
print(re.match('f..','seafood')) # 匹配不到返回None
print(m.group())                 # 返回匹配的值   
m = re.search('f..','seafood')   #
print(m.group()) 
m = re.findall('f..','seafood is food') # 返回所有的匹配项的组成的列表
print(m)
result = re.finditer('f..','seafood is food') # 返回匹配对象组成的迭代器
for i in result:  # 逐个的取出匹配对象
    print(i.group()) 

x = re.sub('f..','abc','fish is food')
print(x)
y = re.split('\.|-','hello-world.tar.gz') # 用.和-做切割的符号
print(y)

patt = re.compile('f..')    # # 先把要匹配的模式编译，提升效率
m = patt.search('seafood')  # 指定在哪个字符串中匹配
print(m.group())

