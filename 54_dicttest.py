#!/usr/bin/env python3

from getpass import getpass
from re  import search

userdb = {}

def register():
    username = input('username: ') 
    if username in userdb:
        print('%s already exits.' % username )
    else:
        password = input('password: ')
        userdb[username] = password 
def login():
    username = input('username: ') 
    password = getpass('password: ')
    if userdb.get(username) != password:
        print('login fail')
    else:
        print('login successful ')
def show_menu():
    cmds = {'_1': register ,'_2': login}
    promt = ''' 1 register
2 login
q exit
please input your choice(1/2/q): '''
    while True:
        choice  =  '_' + input(promt).strip()
        m = search('^_[12q]$',choice)
        if not m:
            print('Invalid input,try again.')
            continue 
        elif choice == '_q':
            break
        cmds[choice]()
if __name__ == '__main__':
    show_menu()
               


            


    
        
        

