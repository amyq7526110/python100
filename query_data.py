#!/usr/bin/env python3
from sqlam_data import Stuinfo,Session

session = Session()
query1 = session.query(Stuinfo.stu_id,Stuinfo.stu_name,Stuinfo.stu_sex)
print(query1)
for stu in query1:
    print(stu)
    print('%s ' % stu.stu_id)
print('-' * 30)
query2 = session.query(Stuinfo.stu_name.label('姓名'))
print(query2)
for stu in query2:
    print(stu.姓名)
print('-' * 30)
query3 = session.query(Stuinfo).order_by(Stuinfo.stu_id)
for stu in query3:
    print(stu)
    print('name: %s  sex: %s' % (stu.stu_name,stu.stu_sex))

query4 = session.query(Stuinfo).order_by(Stuinfo.stu_id)[1:3]
for stu in query4:
    print(stu)
    print('name: %s  sex: %s sid: %s' % (stu.stu_name,stu.stu_sex,stu.stu_id))
print('-' * 30)
query5 = session.query(Stuinfo).filter(Stuinfo.stu_id==3)
print(query5.one())
print('-' * 30)
query6 = session.query(Stuinfo).filter(Stuinfo.stu_id>=2)\
    .filter(Stuinfo.stu_id<4)
for stu in query6:
    print(stu)
    print('name: %s  sex: %s sid: %s' % (stu.stu_name,stu.stu_sex,stu.stu_id))
print('-' * 30)
query7 = session.query(Stuinfo).filter(Stuinfo.stu_name.in_(['小红','张三']))
for stu in query7:
    print(stu)
    print('name: %s  sex: %s sid: %s' % (stu.stu_name,stu.stu_sex,stu.stu_id))
print('-' * 30)
query8 = session.query(Stuinfo).filter(~Stuinfo.stu_name.in_(['小红','张三']))
for stu in query8:
    print(stu)
    print('name: %s  sex: %s sid: %s' % (stu.stu_name,stu.stu_sex,stu.stu_id))
print('-' * 30)
from sqlalchemy import  and_,or_
query10 = session.query(Stuinfo)\
    .filter(and_(Stuinfo.stu_id>=1,Stuinfo.stu_id<4))
for stu in query10:
    print(stu)
    print('name: %s  sex: %s sid: %s' % (stu.stu_name,stu.stu_sex,stu.stu_id))
print('-' * 30)
query11 = session.query(Stuinfo)\
    .filter(or_(Stuinfo.stu_id<=1,Stuinfo.stu_id>4))
for stu in query11:
    print(stu)
    print('name: %s  sex: %s sid: %s' % (stu.stu_name,stu.stu_sex,stu.stu_id))
print('-' * 30)
query12 = session.query(Stuinfo)
print(query12.all())
# for stu in query12.all():
#     print(stu)
#     print('name: %s  sex: %s sid: %s' % (stu.stu_name, stu.stu_sex, stu.stu_id))
print(query12.first())
print('-' * 30)
query13 = session.query(Stuinfo.stu_id,Stuinfo.stu_name).filter(Stuinfo.stu_id==4)
print(query13.one())
print(query13.scalar())
print('-' * 30)
query14 = session.query(Stuinfo).count()
print(query14)
query14 = session.query(Stuinfo)
print(query14.count())
print('-' * 30)
from sqlam_data import Jfb
# zs = Jfb(
#     stu_id = 1,
#     jq = 'y'
# )
# lisi = Jfb(
#     stu_id = 2,
#     jq = 'n'
# )
# ww = Jfb(
#     stu_id=3,
#     jq = 'y'
# )
# xh = Jfb(
#     stu_id = 4,
#     jq = 'n'
# )
# data = [ zs,lisi,ww,xh ]
# session.add_all(data)
# session.commit()
query15 = session.query(Stuinfo.stu_name,Jfb.jq)\
    .join(Jfb,Jfb.stu_id==Stuinfo.stu_id)
print(query15.all())
print('-' * 30)
# session.commit()
session.close()