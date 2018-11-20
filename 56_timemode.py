#!/usr/bin/env python3

import time 

t = time.localtime()  # 返回当前时间的九元组

print(time.gmtime())         # 返回格林威治0时区当前时间的九元组
print(time.time())           # 常用。与1970-1-1 8:00之间的秒数，时间戳
print(time.mktime(t))        # 把九元组时间转成时间戳
time.sleep(1)          
print(time.asctime())        # 如果有参数，是九元组的形式
print(time.ctime())          # 返回当前时间，参数是时间戳，常用
print(time.strftime("%Y-%m-%d"))   # 常用
print(time.strptime('2018-07-20',"%Y-%m-%d"))   # 返回九元组
print(time.strftime("%H:%M:%S"))    



# time.struct_time(tm_year=2018, tm_mon=11, tm_mday=17, tm_hour=3, tm_min=45, tm_sec=14, tm_wday=5, tm_yday=321, tm_isdst=0
# 1542426314.7195125
# 1542426314.0
# Sat Nov 17 11:45:15 2018
# Sat Nov 17 11:45:15 2018
# 2018-11-17
# time.struct_time(tm_year=2018, tm_mon=7, tm_mday=20, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=201, tm_isdst=-1)
# 11:45:15
#  

from datetime import datetime
from datetime import timedelta

print(datetime.today())  # 返回当前时间的datetime对象
print(datetime.now())    # 同上，可以用时区作参数
print(datetime.strptime('2018/06/30', '%Y/%m/%d'))  # 返回datetime

dt  = datetime.today()
print(datetime.ctime(dt))
print(datetime.strftime(dt,"%Y%m%d"))

days = timedelta(days=90,hours=3)  # 返回datetime对象
print(days)

dt2 = dt + days
print(dt2.year)
print(dt2.month)
print(dt2.day)
print(dt2.hour)


#  2018-11-17 11:45:15.735677
#  2018-11-17 11:45:15.735719
#  2018-06-30 00:00:00
#  Sat Nov 17 11:45:15 2018
#  20181117
#  90 days, 3:00:00
#  2019
#  2
#  15
#  14



