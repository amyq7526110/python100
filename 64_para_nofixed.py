#!/usr/bin/env python3


# 64-参数个数不固定的函数

def func1(*args):  # *args是个元组
    print(args)

def func2(**kwargs):  #  **kwargs表示是个字典
    print(kwargs)

def func3(x,y):
    print(x * y)

def func4(name,age):
    print("%s is %s years old" % (name, age))

if __name__ == '__main__':
    func1()
    func1(10)
    func1(10, 'bob')
    func2()
    func2(name='bob', age=25)
    func3(*[10, 5])  # 调用的时候，*表示拆开后面的数据类型
    func4(**{'name': 'bob', 'age': 25})  # name='bob', age=25

  
#  ()
#  (10,)
#  (10, 'bob')
#  {}
#  {'name': 'bob', 'age': 25}
#  50
#  bob is 25 years old

