#!/usr/bin/env python3

# 10 + 5 的结果放到列表中
print([ 10 + 5 ])

# 10 + 5 这个表达式计算10次

print([ 10 + 5 for i in range(10)]) 
print([ 10 + 5 for i in range(1,11)])

# 通过if过滤，满足if条件才参与10+i次的运算

print([ 10 + i for i in range(1,11) if i % 2 == 1])
print([ 10 + i for i in range(1,11) if not  i % 2])

# 生成ip地址列表

print([ '192.168.1.%s' % i for i in range(1,20) ])
