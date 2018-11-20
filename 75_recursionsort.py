#!/usr/bin/env python3
from random import choice,randint

def recusort(a):
    if len(a) < 2:
       return a
    smaller = []
    lager = []
    middle =   a[0]
    print(middle)
    for i in a[1:]:
        if i > middle:
            lager.append(i)
        else:
            smaller.append(i)
    print(smaller)
    print(lager)
    return recusort(smaller)  + [ middle ] +  recusort(lager)       
if __name__ == '__main__':
    alist = [randint(1, 100) for i in range(10)]
    print(alist)
    print(recusort(alist))
    

