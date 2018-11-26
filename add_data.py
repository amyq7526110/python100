#!/usr/bin/env python3
from sqlam_data import Stuinfo,Session

session = Session()

zs = Stuinfo(stu_name='张三',stu_sex='男')
lisi = Stuinfo(stu_name='李斯',stu_sex='男')
ww = Stuinfo(stu_name='王五',stu_sex='男')
xh = Stuinfo(stu_name='小红',stu_sex='女')

stu = [ lisi , ww , xh ]

session.add(zs)
session.add_all(stu)
session.commit()
session.close()