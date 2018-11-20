#!/usr/bin/env python3

# 50-字典基础用法

adict = dict() 
print(adict)   #  {}
print(dict(['ab', 'cd']))
bdict = dict([('name','bob'),('age',25)])
print(bdict)
print({}.fromkeys(['zhangsan','lisi','wangwu'],1))

for key in bdict:
    print('%s: %s ' % (key,bdict[key]))
print('%(name)s: %(age)s' % bdict )    

bdict['name'] = 'tom'
print(bdict)
bdict['email'] = 'tom@tedu.cn'
print(bdict)

del bdict['email']
print(bdict)
bdict.pop('age')
print(bdict)
bdict.clear()
print(bdict)

# {}
# {'a': 'b', 'c': 'd'}
# {'name': 'bob', 'age': 25}
# {'zhangsan': 1, 'lisi': 1, 'wangwu': 1}
# name: bob 
# age: 25 
# bob: 25
# {'name': 'tom', 'age': 25}
# {'name': 'tom', 'age': 25, 'email': 'tom@tedu.cn'}
# {'name': 'tom', 'age': 25}
# {'name': 'tom'}
# {}

