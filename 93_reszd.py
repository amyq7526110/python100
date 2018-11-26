#!/usr/bin/env python3
import re 

def count_patt(fname,patt):
    cpatt = re.compile(patt)
    result = {}

    with open(fname)  as fobi:
        for line in fobi:
            m = cpatt.search(line)  # 如果匹配不到 返回None
    
            if m:
                key = m.group()
    
                result[key] = result.get(key, 0) + 1
    
    return result 

if __name__ == '__main__':
    fname = 'access_log'  # apache的日志文件

    ip = '^(\d{1,3}\.){3}\d{1,3}'   # 日志文件开头的ip地址

    print(count_patt(fname,ip))

    br = 'Firefox|MSIE|Chrome'  # 日志中的客户端

    print(count_patt(fname,br))
