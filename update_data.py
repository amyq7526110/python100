#!/usr/bin/env python3
from sqlam_data import Stuinfo,Session

session = Session()
# q1 = session.query(Stuinfo).filter(Stuinfo.stu_name=='小红')
# stu = q1.one()
# print(stu)
# stu.stu_name='露西'
# session.commit()
cha = session.query(Stuinfo)
for stu in cha:
    print(stu)

# xm = Stuinfo(
#     stu_name = '小明',
#     stu_sex = '男'
# )
#
# session.add(xm)
# session.commit()
# my name is 张三 学号:1
# my name is 李斯 学号:2
# my name is 王五 学号:3
# my name is 露西 学号:4

# my name is 张三 学号:1
# my name is 李斯 学号:2
# my name is 王五 学号:3
# my name is 露西 学号:4
# my name is 小明 学号:5
d1 = session.query(Stuinfo).filter(Stuinfo.stu_name=='小明')
stu = d1.one()
session.delete(stu)
session.commit()
cha = session.query(Stuinfo)
for stu in cha:
    print(stu)
session.close()

# my name is 张三 学号:1
# my name is 李斯 学号:2
# my name is 王五 学号:3
# my name is 露西 学号:4
# my name is 小明 学号:5

# my name is 张三 学号:1
# my name is 李斯 学号:2
# my name is 王五 学号:3
# my name is 露西 学号:4