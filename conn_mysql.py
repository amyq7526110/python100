#!/usr/bin/env python3
import pymysql 

conn = pymysql.connect(
host = '192.168.1.51',
port = 3306,
user = 'root',
passwd = 'Azsd1234.',
db = 'nsd1806',
charset = 'utf8'
)
cur = conn.cursor()
# insert1 = 'insert into departments  values(%s,%s)'
# data = (1,'HR')
# deps = [(5,'HE'),(6,'HO')]
# cur.execute(insert1,data)
# cur.executemany(insert1,deps)
# conn.commit()
# query1 = 'select * from departments order by dep_id '
# cur.execute(query1)
# result = cur.fetchall()
# print(result)
# update1 = 'update departments set dep_name=%s where dep_name=%s'
# data = ('CEO','HO')
# cur.execute(update1,data)
# conn.commit()
delete1 = 'delete from departments where dep_id=%s'
cur.execute(delete1,(5,))
conn.commit()
query1 = 'select * from departments order by dep_id '
cur.execute(query1)
result = cur.fetchall()
print(result)
cur.close()
conn.close()





