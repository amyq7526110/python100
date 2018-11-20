#!/usr/bin/env python3

adict = dict([('name','bob'),('age',25)])
print(len(adict))
print(hash(10))   # 判断给定的数据是不是不可变的,不可变数据才能作为key
print(adict.keys())
print(adict.values())
print(adict.items())
# get 方法常用，重要
adict.get('name')  # 取出字典中name的值如果没有则返回none
print(adict.get('qq'))  # None
print(adict.get('qq','no found'))  # 没有qq，返回指定内容
print(adict.get('age','no found'))
adict.update({'phone':'1234567'})
print(adict)

#   2
#   10
#   dict_keys(['name', 'age'])
#   dict_values(['bob', 25])
#   dict_items([('name', 'bob'), ('age', 25)])
#   None
#   no found
#   25
#   {'name': 'bob', 'age': 25, 'phone': '1234567'}





