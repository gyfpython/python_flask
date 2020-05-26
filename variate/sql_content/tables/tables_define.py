import datetime

from variate.sql_content.base_database import db


class Users(db.Model):

    # Columns

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.VARCHAR(100))
    updateBy = db.Column(db.VARCHAR(100), default='admin')
    account = db.Column(db.VARCHAR(100))
    email = db.Column(db.VARCHAR(100))
    password = db.Column(db.VARCHAR(512))
    createBy = db.Column(db.VARCHAR(100), default='admin')
    createTime = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, username, account, email, password):
        self.username = username
        self.account = account
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.name

    def __str__(self):
        return '<User %s>' % self.name


class Entry(db.Model):
    __tablename__ = 'entries'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.VARCHAR(100))
    text = db.Column(db.VARCHAR(512))
    Catalogs = db.Column(db.Integer)
    updateBy = db.Column(db.VARCHAR(100), default='admin')
    createTime = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, title: str, text: str, catalogs: int, update_by: str = 'admin'):
        self.title = title
        self.text = text
        self.Catalogs = catalogs
        self.updateBy = update_by


class Catalogs(db.Model):
    __tablename__ = 'catalogs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    catalogName = db.Column(db.VARCHAR(45), unique=True)
    catalogNumber = db.Column(db.Integer, unique=True)
    createBy = db.Column(db.VARCHAR(45))
    createTime = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, catalog_name: str, catalog_number: int, create_by: str):
        self.catalogName = catalog_name
        self.catalogNumber = catalog_number
        self.createBy = create_by
