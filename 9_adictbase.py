#!/usr/bin/env python3

#  字典是key-value(键－值）对形式的，没有顺序，通过键取出值

adict1 = {'name':'bob','age':23}
print(adict1)
print(len(adict1))                 # 2
print('bob' in adict1)             # False 
print('name' in adict1)            # True
adict1['email'] = 'bob@tedu.cn'    # 字典中没有key，则添加新项目 
adict1['age'] = 25                 # 字典中已有key，修改对应的value      
print(adict1)


