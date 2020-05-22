from sqlalchemy import Column, Integer, VARCHAR, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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


class Entry(Base):
    __tablename__ = 'entry'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(VARCHAR(100))
    text = Column(VARCHAR(512))
    Catalogs = Column(Integer)
    updateBy = Column(VARCHAR(100), default='admin')
    createTime = Column(DateTime, default='1970-01-01 00:00:00')


class Catalogs(Base):
    __tablename__ = 'catalogs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    catalogName = Column(VARCHAR(45), unique=True)
    catalogNumber = Column(Integer, unique=True)
    createBy = Column(VARCHAR(45))
    createTime = Column(DateTime, default='1970-01-01 00:00:00')


# engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1:3306/flask')
#
#
# DBSession = sessionmaker(bind=engine)
# session = DBSession()
# lalala = session.query(Users.username).filter_by(id=20).all()
# session.commit()
# print(lalala)

# new_user = Users(username='test1', account="test1", email="test1@123.com",
#                  password='123123123', createTime=datetime.datetime.now())
# session.add(new_user)
# session.commit()
# 关闭 session:
# session.close()
