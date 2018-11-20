#!/usr/bin/env python3


print('%s is %s years old' % ('bob',20))      #  bob is 20 years old
print() #  常用                               #  
print('%s is %d years old' % ('lucy',23))     #  lucy is 23 years old
print() #  常用                               #  
print('%s is %d years old' % ('bob', 23.5))   #  bob is 23 years old
print() #  %d 是整数                          #  
print('%s is %f years old' % ('bob',23.5))    #  bob is 23.500000 years old
print('%s is %5.2f years old' % ('bob',23.5)) #  bob is 23.50 years old
print() #  %5.2f 是宽度5 ，两位小数           #  
print('97 is %c'  % 97)                       #  97 is a
print('11 is %#o' % 11)                       #  11 is 0o13
print() # %#o表示有前缀的8进制                #  
print('11 is %#x' % 11)                       #  11 is 0xb
print('%10s%5s'   % ('name','age'))           #        name  age
print() # %10s表示总宽度为10，右对齐，常用    #  
print('%10s%5s'   % ('bob',23))               #         bob   23
print('%10s%5s'   % ('alser',35))             #       alser   35
print('%-10s%-5s' % ('name','age'))           #  name      age  
print() # %-10s表示总宽度为10，左对齐，常用   #  
print('%-10s%-5s'   % ('bob',23))             #  bob       23   
print('%10d' % 123)                           #         123
print('%010d' % 123)                          #  0000000123
print('{} is {} years old'.format('boy',25))  #  boy is 25 years old
print('{1} is {0} years old'.format('boy',25))#  25 is boy years old
print('{:<10}{:<8}'.format('name','age'))     #  name      age  
