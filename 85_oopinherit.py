#!/usr/bin/env python3

#  如果两个类有很多相同之处，使用继承更为合理。
#  新品玩具熊增加了一个跑的行为，其他与原来的玩具熊一致。

class BearToy:
    def __init__(self,nm,color,size):
        self.name = nm
        self.color = color   # 绑定属性到实例
        self.size = size
    def sing(self):
        print('lalala........')
    def speak(self):
        print('My name is %s' % self.name)
class NewBear(BearToy):
    def run(self):
        print('running....')

if __name__ == '__main__':
    b1 = NewBear('venie','Yellow','Bigger')
    b1.sing()
    b1.run()

         
