#!/usr/bin/env python3
import random

# 17_改进石头剪刀布

all_choices = ['石头','剪刀','布']
win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]
computer = random.choice(all_choices)

potal = '''
0  石头
1  剪刀
2  布
请出拳  : ''' 
pwin = 0
cwin = 0
while pwin < 2  and cwin < 2:
    player = all_choices[int(input(potal))]
    print('\033[31m')
    print("Your choice: %s, Computer's choice: %s" % (player, computer))
    
    if player == computer:
        print('平局')
    elif [player,computer] in win_list:
        print('You win !')
        pwin += 1 
    else:
        print('You lose')
        cwin += 1
    print('\033[0m')








 


