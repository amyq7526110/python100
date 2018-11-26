#!/usr/bin/env python3
class Book:
    def __init__(self,title,auter,pages):
        self.title = title
        self.auter = auter
        self.pages = pages
    def __str__(self):
        return '<<%s>>' % self.title
    def __call__(self):
        print('<<%s>> is wirten by %s ' % (self.title,self.auter)) 

if __name__ == '__main__':
    py_book = Book('Core Python','Wesley' , 800) # 调用__init__()方法
    print(py_book)  # 调用 __str__  方法
    py_book()       # 调用 __call__ 方法


