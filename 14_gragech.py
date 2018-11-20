#!/usr/bin/env python3

score = int(input('分数:> '))
print('\033[31m')
if score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 70:
    print('良')
elif score >= 60:
    print('及格')
else:
    print('没救了')
print('\033[0m')
