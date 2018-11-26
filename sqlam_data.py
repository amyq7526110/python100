#!/usr/bin/env python3
from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Date,ForeignKey,Enum
from sqlalchemy.orm import  sessionmaker

engine = create_engine(
    'mysql+pymysql://root:Azsd1234.@192.168.1.51/test?charset=utf8',
    encoding='utf8',
 #  echo = True
)

Session = sessionmaker(bind=engine)
Base = declarative_base()



class Stuinfo(Base):
    __tablename__ = 'stuinfo'
    stu_id = Column(Integer,primary_key=True)
    stu_name = Column(String(20),nullable=False)
    stu_sex = Column(Enum('男','女'),default='男')
    def __str__(self):
       return  'my name is %s 学号:%s ' % (self.stu_name,self.stu_id)

class Jfb(Base):
    __tablename__ = 'jfb'
    jq = Column(Enum('y','n'),nullable=False,default='n')
    stu_id = Column(Integer,ForeignKey('stuinfo.stu_id'))
    auto_id = Column(Integer,primary_key=True)

if __name__ == '__main__':
    Base.metadata.create_all(engine)