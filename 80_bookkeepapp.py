#!/usr/bin/env python3
import pickle 
import os
import time
import re

def cost(wallet,record):  # 记录花钱的函数
    amount = int(input('amount: '))
    comment = input('comment: ')
    date = time.strftime('%Y-%m-%d')
    with open(wallet,'rb') as fobj:
        balance = pickle.load(fobj) - amount
    with open(wallet,'wb') as fobj:
        pickle.dump(balance,fobj)
    with open(record,'a') as fobj:
        fobj.write(
            '%-12s%-8s%-8s%-10s%-20s\n' % (date, '', amount, balance, comment)
            )
def save(wallet,record):  # 记录存钱的函数
    amount = int(input('amount: '))
    comment = input('comment: ')
    date = time.strftime('%Y-%m-%d')
    with open(wallet,'rb') as fobj:
        balance = pickle.load(fobj) + amount
    with open(wallet,'wb') as fobj:
        pickle.dump(balance,fobj)
    with open(record,'a') as fobj:
        fobj.write(
            '%-12s%-8s%-8s%-10s%-20s\n' % (date, '', amount, balance, comment)
            )
def query(wallet,record):  # 查明收支明系的函数
    print('%-12s%-8s%-8s%-10s%-20s' % ('date', 'cost', 'save', 'balace', 'comment'))
    with open(record) as fobj:
        # print(balance)
        for line in fobj:
            print(line,end='')
    with open(wallet,'rb')  as fobj:
        balance = pickle.load(fobj)
    print('Latest Balance: %d' % balance)    
    
def show_menu():
    cmds = {'_1':cost,'_2':save,'_3':query}
    prompt = '''\033[36m(1) cost
(2) save
(3) query
(q) exit
Please input your choice(1/2/3/q): \033[0m'''
    wallet = 'wallet.data'
    record = 'record.txt'
    if not os.path.exists(wallet):
        with open(wallet,'wb') as fobj:
            pickle.dump(10000,fobj)
    while True:
        choice = '_' + input(prompt).strip()
        result = re.search(r'^_[123q]$',choice)
        if not result:
            print('Invalid input ,Try again.')

            continue
        elif choice == '_q':
            break
        cmds[choice](wallet,record)

if __name__ == '__main__':
    show_menu()
    
