#!/usr/bin/env python3
sentence = 'tom\'s pet is a cat ' # 单引号中间还有单引号，可以转义
sentence2 = "tom's pet is a cat "  # 也可以用双引号包含单引号
sentence3 = "tom said:\"hello world\" "  
sentence4 = 'tom said:"hello world" '
# 三个连续的单引号或双引号，可以保存输入格式，允许输入多行字符串
word = """
hello 
world 
abcd """
print(word)

py_str = 'python'
print(len(py_str))  # 取长度
print(py_str[0])    # 第一个字符
print('python'[0])
print(py_str[-1])   # 最后一个字符
# print(py_str[6])  # 错误超出下标
print(py_str[2:4])  # 切片，起始下标包含，结束下标不包含
print(py_str[2:])   # 从下标为2的字符取到结尾
print(py_str[:2])    # 从开头取到下标是2之前的字符
print(py_str[:])    # 取全部
print(py_str[::2])  # 步长值为2,默认为1
print(py_str[1::2]) # 取出‘yhn’   
print(py_str[::-1]) # 步长为负，表示自右向左取
print(py_str + 'is good')  # 简单的拼接
print(py_str * 3)   #  把字符串重复3遍
print(py_str * 3)  #  ^

print('t' in py_str)        # True
print('th' in py_str)       # True
print('to' in py_str)       # False
print('to' not  in py_str)  # False











 

