#!/usr/bin/env python3
import sys

def unix2doc(fname):
    dsf_fame = fname + '.txt'
    
    with open(fname) as src_fobj:
        with open(dsf_fame,'w') as dst_fobj:
            for line in src_fobj:
                line = line.rstrip() + '\r\n'
                dst_fobj.write(line)
if __name__ == '__main__':
    unix2doc(sys.argv[1])
                
