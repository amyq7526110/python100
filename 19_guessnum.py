#!/usr/bin/env python3
import random

number = random.randint(1,10)
count = 0  
while count < 5  : 
    answer = int(input('guess the number: '))
    if answer > number:
       print('猜大了')
    elif answer < number:
       print('猜小了')
    else:
       print('猜对了')
       break
    count += 1
else:      #  循环被break就不执行了，没有被break才执行
    print("the number is %s" % number)

 
   
