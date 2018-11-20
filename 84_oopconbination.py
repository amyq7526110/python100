#!/usr/bin/env python3

class Vendor:
    def __init__(self,phone,email):
        self.phone  = phone
        self.email = email

    def call(self):
        print('calling %s ' % self.phone)

class BearToy:
    def __init__(self,color,size,phone,email):
        self.color = color  # 绑定实例
        self.size = size
        self.vendor = Vendor(phone,email)

if __name__ == '__main__':
    bigbear = BearToy('Brown','Middle','400-111-0099','haha@tedu.cn')
    print(bigbear.color)
    bigbear.vendor.call()

