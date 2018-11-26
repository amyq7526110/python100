#!/usr/bin/env python3
#  如果子类和父类具有同名的方法，那么父类方法将被遮盖住。
#  可以在子类中明确指明调用的是父类方法，而不是子类的同名方法。

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
    def __init__(self,nm,color,size,date):
        BearToy.__init__(self,nm,color,size) # 以下写法完全一样，更推荐下面写法
        # super(NewBear,self).__init__(nm,color,size)
        self.date = date #  新品玩具熊增加玩具熊的生产日期
    def run(self):
        print('running........')
if __name__ == '__main__':
    b1 = NewBear('venie','Yellow','Bigger','2018-05-30')
    print(b1.date)
    b1.sing()
    b1.run()

         
