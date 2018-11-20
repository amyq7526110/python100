#!/usr/bin/env python3


py_str = 'hello world!'
print(py_str)                             #hello world!
print(py_str.capitalize())                #Hello world!
print(py_str.title())                     #Hello World!
print(py_str.center(50))                  #                    hello world!                   
print(py_str.center(50, '#'))             # ###################hello world!###################
print(py_str.ljust(50, '*'))              # hello world!**************************************
print(py_str.rjust(50, '*'))              # **************************************hello world!
print(py_str.count('l'))   
# 统计l出现的次数                         # 3
print(py_str.count('lo'))  
#                                         # 1
print(py_str.endswith('!')) 
# # 以!结尾吗？                           # True
print(py_str.endswith('d!'))
#                                         # True
print(py_str.startswith('a'))             
# 以a开头吗                               # False
print(py_str.islower())    
# 字母都是小写的吗 其他不考虑             # True
print(py_str.isupper())  
# 字母都是大写的吗 其他不考虑             # False
print('Hao123'.isdigit()) 
# 所有字符的都是数字吗                    # False
print('Hao123'.isalnum()) 
# 所有字符都是字母 数字吗                 # True
print(' hello\t   '.strip())
# 去除两端空白字符,常用                   # hello
print(' hello\t   '.lstrip())             # hello   
print(' hello\t   '.rstrip())             #  hello
print('how are you?'.split())             # ['how', 'are', 'you?']
print('hello.tar.gz'.split('.'))          # ['hello', 'tar', 'gz']
print('.'.join(['hello','tar','gz']))     # hello.tar.gz
print('-'.join(['hello','tar','gz']))     # hello-tar-gz


























