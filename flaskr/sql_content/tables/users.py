from sqlalchemy import Column, Integer, VARCHAR, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()


class Users(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(VARCHAR(100))
    updateBy = Column(VARCHAR(100), default='admin')
    account = Column(VARCHAR(100))
    email = Column(VARCHAR(100))
    password = Column(VARCHAR(512))
    createBy = Column(VARCHAR(100), default='admin')
    createTime = Column(DateTime, default='1970-01-01 00:00:00')


engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1:3306/flask')


# 创建 DBSession 类型:
DBSession = sessionmaker(bind=engine)
# 创建 session 对象:
session = DBSession()

# 创建 Player 对象:
new_user = Users(username='test1', account="test1", email="test1@123.com",
                 password='123123123', createTime=datetime.datetime.now())
# 添加到 session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭 session:
session.close()
