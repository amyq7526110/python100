#!/usr/bin/env python3

import time
import os 

def calc():
    result = 0
    for i in range(1,50000001):
        result += 1
    print(result)        

if __name__ == '__main__':
    start = time.time()
    for i in range(2):
        pid = os.fork()
        if not pid:
            calc()
            exit()                
    os.waitpid(-1,0)        
    os.waitpid(-1,0)        
    end = time.time()
    print(end - start)

