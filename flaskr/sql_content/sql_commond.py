from flaskr.mysql_operation.mysql_connection import MysqlConnection


class SqlCom(object):
    def __init__(self, database: MysqlConnection):
        self.database = database

    # table users
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

    # table entries
    def get_all_entry_creator(self):
        get_creator = "select distinct updateBy from entries;"
        results = self.database.select_data(get_creator)
        if results:
            return [result[0] for result in results]
        return None

    # table catalogs
    def get_all_catalog_code(self):
        get_creator = "select distinct catalogNumber, catalogName from catalogs;"
        results = self.database.select_data(get_creator)
        if results:
            return results, [result[0] for result in results]
        return None




