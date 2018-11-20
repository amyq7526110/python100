#!/usr/bin/env python3
score = int(input('分数:> '))
print('\033[31m')
if score >= 60 and score < 70:
    print('及格')
elif  80  >  score >= 70 :
    print('良')
elif  80 <= score <90 :
    print('良好')
elif score >= 90:
    print('优秀')
else:
    print('没救了')
print('\033[0m')
