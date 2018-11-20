#!/usr/bin/env python3
import tkinter
from functools import partial

def hello():
    lb.config(text='Hello China!' )
def welcome():
    lb.config(text='Hello tedu!')
def bibao(word):
    def wlc():
        lb.config(text='Hello %s' % word)
    return wlc     #  # hello函数的返回值还是函数


root = tkinter.Tk()

lb = tkinter.Label(text='Hello World',font='Times 26')
MyBtn = partial(tkinter.Button,root,fg='white',bg='blue')
b1 = MyBtn(text='Button 1', command=bibao('lele'))
b2 = MyBtn(text='Button 2', command=bibao('haha'))
b3 = MyBtn(text='quit', command=root.quit)
lb.pack()
b1.pack()
b2.pack()
b3.pack()
root.mainloop()

