#!/usr/bin/env python3

# 39-序列对象方法2

alist = [ 10 , 'john' ]

#  list(enumerate(alist))  # [(0, 10), (1, 'john')]

print(list(enumerate(alist))) 

a, b = 0, 10   # a->0  ->10

print(a,b)   

for ind in range(len(alist)):
    print('%s : %s ' % (ind,alist[ind]))

for item in enumerate(alist):
    print('%s : %s' %  (item[0],item[1]))

for ind,val in enumerate(alist):
    print('%s : %s' %  (ind,val))
     
atuple = (96, 97, 40, 75, 58, 34, 69, 29, 66, 90)

print(sorted(atuple))

print(sorted('hello'))

for i in reversed(atuple):
    print(i,end=',')
print()


#  0 : 10 
#  1 : john 
#  0 : 10
#  1 : john
#  0 : 10
#  1 : john
#  [29, 34, 40, 58, 66, 69, 75, 90, 96, 97]
#  ['e', 'h', 'l', 'l', 'o']
#  90,66,29,69,34,58,75,40,97,96,


