#!/usr/bin/env python3

# 通过Date创建实例，也可以通过Date.create创建实例

class Date:
    def __init__(self,year,month,date):
        self.year = year
        self.month = month
        self.date = date
    @classmethod  # 类方法，不用创建实例即可调用
    def create(cls,dstr):  # cls 表示 类本身,class 的缩写
        y,m,d = map(int ,dstr.split('-')) # map(int , [ '2000','5','4'])
        dt = cls(y,m,d)  # 即Date(y,m.d)
        return dt
    @staticmethod  # 静态方法 写在类的外面，可以独立的成为一个函数,就是函数
    def is_date_valid(dstr):
        y,m,d = map(int,dstr.split('-'))
        return  y < 4000 and 0 <  m  < 13  and 0  < d < 32

if __name__ == '__main__':
    bith_date = Date(1995,12,3)
    print(Date.is_date_valid('2000-12-33'))
    day = Date.create('2001-03-12')
    print(day.year)
    print(day.month)
    print(day.date)
