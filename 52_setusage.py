#!/usr/bin/env python3


# 集和相当于无值的字典，所以也用{}表示
myset = set('hello')
print(myset)
print(len(myset))
for ch in myset:
    print(ch)
aset = set('abc')
bset = set('cde')
print('aset = %s  bset  = %s ' % ( aset , bset))
print(aset & bset)             # 交集
print(aset.intersection(bset))  # 交集
print(aset | bset)             # 并集
print(aset.union(bset))        # 并集
print(aset - bset)             # 差补
print(aset.difference(bset))   # 差补
aset.add('new')         
print(aset)
aset.update(['aaa','bbb'])
print(aset)
aset.remove('bbb')
print(aset)
cset = set('abcde')
dset = set('bcd')
print(cset.issuperset(dset))  # cset是dest 的超集吗
print(cset.issubset(dset))     # cset是dset 的子集吗 


#  {'l', 'h', 'o', 'e'}
#  4
#  l
#  h
#  o
#  e
#  aset = {'c', 'b', 'a'}  bset  = {'c', 'e', 'd'} 
#  {'c'}
#  {'c'}
#  {'a', 'c', 'e', 'b', 'd'}
#  {'a', 'c', 'e', 'b', 'd'}
#  {'b', 'a'}
#  {'b', 'a'}
#  {'c', 'b', 'a', 'new'}
#  {'a', 'aaa', 'c', 'new', 'bbb', 'b'}
#  {'a', 'aaa', 'c', 'new', 'b'}
#  True
#  False





