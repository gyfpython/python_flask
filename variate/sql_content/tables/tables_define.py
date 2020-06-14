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
    roleCode = db.Column(db.Integer)
    password = db.Column(db.VARCHAR(512))
    createBy = db.Column(db.VARCHAR(100), default='admin')
    createTime = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, username, account, email, password, role_code):
        self.username = username
        self.account = account
        self.email = email
        self.password = password
        self.roleCode = role_code

    def __repr__(self):
        return '<User %r>' % self.username

    def __str__(self):
        return '<User %s>' % self.username


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


class Roles(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roleName = db.Column(db.VARCHAR(45), unique=True)
    roleCode = db.Column(db.Integer, unique=True)
    description = db.Column(db.VARCHAR(45))
    createBy = db.Column(db.VARCHAR(45))
    createTime = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, role_name: str, role_code: int, create_by: str, description: str):
        self.roleName = role_name
        self.roleCode = role_code
        self.createBy = create_by
        self.description = description


class Permissions(db.Model):
    __tablename__ = 'permissions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    permissionName = db.Column(db.VARCHAR(45), unique=True)
    permissionCode = db.Column(db.Integer, unique=True)
    parentPermissionCode = db.Column(db.Integer)
    description = db.Column(db.VARCHAR(45))
    createBy = db.Column(db.VARCHAR(45))
    createTime = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, permission_name: str, permission_code: int,
                 parent_code: int, create_by: str, description: str):
        self.permissionName = permission_name
        self.permissionCode = permission_code
        self.createBy = create_by
        self.description = description
        self.parentPermissionCode = parent_code


class RolePermissions(db.Model):
    __tablename__ = 'role_permissions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    permission = db.Column(db.Integer)
    roleCode = db.Column(db.Integer)
    createBy = db.Column(db.VARCHAR(45))
    createTime = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, permission: str, role_code: int, create_by: str):
        self.permission = permission
        self.roleCode = role_code
        self.createBy = create_by


class UserRole(db.Model):
    __tablename__ = 'user_role'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.VARCHAR(45))
    roleCode = db.Column(db.Integer)
    createBy = db.Column(db.VARCHAR(45))
    createTime = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, username: str, role_code: int, create_by: str):
        self.username = username
        self.roleCode = role_code
        self.createBy = create_by
