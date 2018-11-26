#!/usr/bin/env python3

# 类的父类（基类）可以有很多个，子类可以调用所有父类的方法。
# 如果有重名方法，生效的顺序是自下而上，自左而右。当然最好不要出现重名方法。

class A:
    def foo(self):
        print('in A foo')
    def hello(self):
        print('A hello')

class B:    
    def bar(self):
        print('in B bar')
    def hello(self):
        print('B hello')

class C(B,A):
    pass
    def hello(self):
        print('C hello')
    
if __name__ == '__main__':
    c = C()
    c.foo()
    c.bar()
    c.hello()



