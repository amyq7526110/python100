#!/usr/bin/env python3
import random

# 16-石头剪刀布

all_choices = ['石头','剪刀','布']

computer = random.choice(all_choices)

potal = '''
0  石头
1  剪刀
2  布
请出拳  : ''' 

player = all_choices[int(input(potal))]
print("Your choice: %s, Computer's choice: %s" % (player, computer))

if player == '石头':
    if computer ==  '石头':
       print('平局')
    elif computer == '剪刀':
       print('You win !')
    else:  
       print('You lose')    
elif player == '剪刀':
    if computer ==  '石头':
       print('You lose')    
    elif computer == '剪刀':
       print('平局')
    else:  
       print('You win !')
else :
    if computer ==  '石头':
       print('You win !')
    elif computer == '剪刀':
       print('You lose')    
    else:  
       print('平局')













 


