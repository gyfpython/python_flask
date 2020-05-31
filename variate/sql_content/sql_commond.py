import datetime

from variate.sql_content.mysql_connection import MysqlConnection
from variate.sql_content.base_database import db
from variate.sql_content.tables.tables_define import *


class SqlCom(object):
    def __init__(self, database: MysqlConnection):
        self.database = database

    # table users
    def add_user(self, username: str, account: str, pwd: str, email: str):
        add_user_sql = "insert into users (username, account, password, email, createTime, updateBy, createBy) " \
                       "values ('{username}', '{account}', '{password}', '{email}', '{createTime}', " \
                       "'{updateBy}', '{createBy}')"\
            .format(username=username, account=account, password=pwd,
                    email=email, createTime=datetime.datetime.now(), updateBy='admin', createBy='admin')
        self.database.connect_db(add_user_sql)

    def check_username(self, username: str):
        get_username_sql = "select username from users where username = '{username}'".format(username=username)
        result = self.database.select_data(get_username_sql)
        if result:
            return True
        return False

    def get_pwd(self, username: str):
        get_pwd_sql = "select password from users where username = '{username}'".format(username=username)
        result = self.database.select_data(get_pwd_sql)
        if result:
            return result[0][0]
        return None

    def get_user_role(self, username: str):
        get_user_role = "select b.roleName, a.roleCode from users a, roles b" \
                        " where a.username = '{username}' and a.roleCode = b.roleCode;".format(username=username)
        result = self.database.select_data(get_user_role)
        if result:
            return result
        return None

    # table entries
    def add_new_entry(self, title: str, text: str, updateBy: str, Catalogs: int):
        sql = "insert into entries (title, text, updateBy, createTime, Catalogs) " \
              "values ('{title}', '{text}', '{user}', '{datetime}', '{catalogs}')"
        sql1 = sql.format(title=title, text=text,
                          user=updateBy, datetime=datetime.datetime.now(), catalogs=Catalogs)
        self.database.connect_db(sql1)

    def delete_a_entry_by_id(self, id: int):
        delete_entry_sql = "delete from entries where id = {id}".format(id=id)
        self.database.connect_db(delete_entry_sql)

    def update_entry(self, title: str, text: str, updateBy: str, Catalogs: int, id: int):
        sql = "update entries set title='{title}', text='{text}', Catalogs={Catalogs}, updateBy='{user}', " \
              "createTime='{datetime}' where id = {id}"
        sql1 = sql.format(title=title, text=text, user=updateBy, Catalogs=Catalogs, datetime=datetime.datetime.now(), id=id)
        self.database.connect_db(sql1)

    def get_all_entry_creator(self):
        get_creator = "select distinct updateBy from entries;"
        results = self.database.select_data(get_creator)
        if results:
            return [result[0] for result in results]
        return None

    def get_all_entry(self):
        get_entry = "select title, text, id from entries order by title"
        results = self.database.select_data(get_entry)
        if results:
            return results
        return None

    def get_filtered_entry(self, search_condition: dict):
        if not search_condition['title']:
            sql = "select title, text, id from entries where Catalogs = %d and updateBy = '%s' order by %s" % \
                  (int(search_condition['catalog']), search_condition['create_by'], search_condition['sort'])
        else:
            sql = "select title, text, id from entries where " \
                  "Catalogs = %d and updateBy = '%s' and title like '%%%s%%' order by %s" % \
                  (int(search_condition['catalog']), search_condition['create_by'],
                   search_condition['title'], search_condition['sort'])
        result = self.database.select_data(sql)
        if result:
            return result
        return None

    def check_entry_id_exist(self, id_int: int):
        try:
            select_by_id = "select title, text, id, Catalogs from entries where id = {id}".format(id=id_int)
            result = self.database.select_data(select_by_id)
            entry = [dict(title=row[0], text=row[1], id=row[2], catalogs=row[3]) for row in result]
            if not entry or len(entry) > 1:
                return False, None
            else:
                entry[0]['text'] = entry[0]['text'].replace('\r\n', '')
                return True, entry
        except Exception as id_error:
            print(id_error)
            return False, None

    # table catalogs
    def get_max_catalog_number(self):
        max_number_sql = "select max(catalogNumber) from catalogs"
        result = self.database.select_data(max_number_sql)
        if result:
            return result[0][0]
        return None

    def add_new_catalog(self, catalog_name: str, catalog_number: int, username: str):
        insert_catalog_sql = "insert into catalogs (catalogNumber, catalogName, createTime, createBy)" \
                             " values ('{catalogNumber}', '{catalogName}', '{createTime}', '{createBy}')".\
            format(catalogNumber=catalog_number, catalogName=catalog_name,
                   createTime=datetime.datetime.now(), createBy=username)
        self.database.connect_db(insert_catalog_sql)

    def get_all_catalog_code(self):
        get_creator = "select distinct catalogNumber, catalogName from catalogs;"
        results = self.database.select_data(get_creator)
        # results1 = Catalogs.query.all()
        if results:
            return results, [result[0] for result in results]
        return None

    # roles
    def get_all_role(self):
        get_roles = "select roleName, roleCode from roles;"
        result = self.database.select_data(get_roles)
        if result:
            return result
        return None

    # permissions
    def get_whole_permission_tree(self):
        get_a_tree_sql = "select permissionName, permissionCode from permissions"
        result = self.database.select_data(get_a_tree_sql)
        if result:
            return result
        return None

    # role_permissions
    def get_rule_permission(self, role_code: int):
        get_rule_permission = "select b.permissionName, a.permission from role_permissions a, permissions b " \
                              "where a.roleCode = {rc} and a.permission = b.permissionCode;".format(rc=role_code)
        result = self.database.select_data(get_rule_permission)
        if result:
            return result
        return None




