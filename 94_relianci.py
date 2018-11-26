#!/usr/bin/env python3

import re

from collections import Counter # # Counter对象是有序的，字典无序

class CountPatt:
    def __init__(self,fname):
        self.fname = fname

    def count_patt(self,patt):
        cpatt = re.compile(patt)
        result = Counter()

        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:
                    result.update([m.group()])

        return result                    

if __name__ == '__main__':
    
    c = CountPatt('access_log')
    ip = '^(\d+\.){3}\d+'
    br = 'Firefox|MSIE|Chrome'

    a = c.count_patt(ip)
    print(a)
    print(a.most_common(3)) # 访问量最大的前三名

    print(c.count_patt(br))


