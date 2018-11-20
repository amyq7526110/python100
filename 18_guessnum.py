#!/usr/bin/env python3
import random

number = random.randint(1,10)
running =True 
while running  : 
    answer = int(input('guess the number: '))
    if answer > number:
       print('猜大了')
    elif answer < number:
       print('猜小了')
    else:
       print('猜对了')
       running = False

