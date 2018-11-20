#!/usr/bin/env python3

def factorial1(x):
    if x == 1:
        return 1
    return  x * factorial1(x-1)       
if __name__ == '__main__':
    print(factorial1(5))

