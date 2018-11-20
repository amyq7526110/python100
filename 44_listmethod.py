#!/usr/bin/env python3
alist = [ 1,2,3,'bob','alice']
print(alist)
alist[0] = 10
print(alist)
alist[1:3] = [20,30]
print(alist)
alist[2:2] = [22,24,26,28]
print(alist)
alist.append(100)  
print(alist)
alist.remove(24)  
print(alist)
# 删除第一个24
alist.index('bob')
print(alist)
# 返回下标
blist = alist.copy()  
# 相当于blist = alist[:] 
alist.pop()
print(alist)
# 默认弹出最后一项
alist.pop(2)
print(alist)
# 默认弹出最后一项
alist.pop(alist.index('bob'))
print(alist)
# alist.sort()
print(alist)
alist.reverse()
print(alist)
print(alist.count(20))
# 统计20在列表中出像的次数
print(alist)
# 清空
alist.append('new')
print(alist)
alist.extend('new')
print(alist)
alist.extend(['hello','world','hehe'])
#print(alist)
print(alist)
