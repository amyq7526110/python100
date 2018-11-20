#!/usr/bin/env python3
import os
def blocks(fobj):
    block = []
    counter = 0
    for line in fobj:
        block.append(line)
        counter += 1
        if counter == 10:
            yield block
            block = []
            counter = 0
    if block: # 文件最后不够10行的部分
         yield block
if __name__ == '__main__':
    os.system('\cp /etc/passwd /tmp/passwd')
    fobj = open('/tmp/passwd') # 
    for lines in blocks(fobj):
        print(lines)
        print()
    fobj.close()


        
