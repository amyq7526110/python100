#!/usr/bin/env python3

from re import search
#  47-列表练习：模拟栈操作

stack = []

def push_it(): 
   item = input('item to push: ')
   stack.append(item)

def pop_it():
    if stact:
       print("from stack poped %s " % stack.pop())
       
def view_it():
    print(stack)
    
def show_menu():
    cmds = {'_1':push_it,'_2':pop_it,'_3':view_it}
    prompt = '''(1) push_it
(2) pop it 
(3) view it 
(q) exit
please input your choice(1/2/3/q): '''
    while True:
       #  input()得到字符串，用strip()去除两端空白，再取下标为0的字符
       choice =  '_' + input(prompt).strip() 
       m = search(r'^_[123q]$',choice)
       if not m:
           print('\033[1mInvalid input ,Try again.\033[0m')
           continue
       if choice == '_q' :    
           break
       
       cmds[choice]()

if __name__ == '__main__':
    show_menu()




           


   
