#!/usr/bin/env python3

def color(func):
    def red():
        return '\033[31m%s\033[0m' % func()
    return red

def hello():
    return 'Hello world'

@color
def welcome():
    return 'Hello China'


if __name__ == '__main__':
    hello = color(hello)    # 此种写法可以换成为welcome加上@color 的写法
    print(hello())
    print(welcome())   # welcome因为有装饰器，所以调用时不是调用welcome函数
                       # 而是相当于color(welcome)()
                       # color(welcome)返回red，color(welcome)()
                       # 等价于red()

