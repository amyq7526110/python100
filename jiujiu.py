#!/usr/bin/env python3
import sys
def jiujiu(x=9):
    for i in range(1,x+1):
        for j in range(1,i+1):       
            print('%s*%s=%s ' % (j,i,i*j),end=' ')
        print()
if __name__ == '__main__':
   try:  
       jiujiu(int(sys.argv[1]))
   except (IndexError,ValueError): 
       print('Usage: %s number' % sys.argv[0])
    
