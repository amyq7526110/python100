#!/usr/bin/env python3

# 列表也是序列对象，但它是容器类型，列表中可以包含各种数据

alist = [ 10,20,30,'bob','alice',[1,2,3] ]
print(alist)
print(len(alist))        # 列表元素个数
print(alist[-1])         # 取出最后一项
print(alist[-1][-1])     # 因为最后一项是列表，列表还可以继续取下标
print([1,2,3][-1])       # [1,2,3]是列表，[-1]表示列表最后一项
print(alist[-2][2])      # 列表倒数第2项是字符串，再取出字符下标为2的字符
print(alist[3:5])        # ['bob','alice'] 
print(10 in alist)       # True
print('o' in alist)      # True
print(100 not in alist)  # True
alist[-1]  = 100         # 修改最后一项的值
alist.append(200)        # 向列表中追加一项
print(alist)
