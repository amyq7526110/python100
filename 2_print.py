#!/usr/bin/env python3

print('hello world')
print('hello','world')    # 逗号自动添加默认的分隔符：空格
print('hello' + 'world')  # 加号表示字符拼接
print('hello','world',sep='***') # 单词间用***分隔
print('#' * 50)           # '#'  重复50遍
print('how are you?',end='') # 默认 end='\n' ,end='' 表示不要回车
help(print)


