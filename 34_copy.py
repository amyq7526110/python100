#!/usr/bin/env python3


import sys 

def copy(src_fname,dst_fname):
    with open(src_fname,"rb") as sf:
        with open(dst_fname,'wb') as df:
             while True: 
                 data = sf.read(4096) 
                 if not data:
                     break
                 df.write(data)


if __name__ == '__main__':
    copy(sys.argv[1],sys.argv[2])
