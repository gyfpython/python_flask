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

    def get_all_entry(self):
        get_entry = "select title, text, id from entries order by title desc"
        results = self.database.select_data(get_entry)
        if results:
            return results
        return None

    def get_filtered_entry(self, search_condition: dict):
        if not search_condition['title']:
            sql = "select title, text, id from entries where Catalogs = %d and updateBy = '%s' order by %s desc" % \
                  (int(search_condition['catalog']), search_condition['create_by'], search_condition['sort'])
        else:
            sql = "select title, text, id from entries where " \
                  "Catalogs = %d and updateBy = '%s' and title like '%%%s%%' order by %s desc" % \
                  (int(search_condition['catalog']), search_condition['create_by'],
                   search_condition['title'], search_condition['sort'])
        result = self.database.select_data(sql)
        if result:
            return result
        return None

    # table catalogs
    def get_all_catalog_code(self):
        get_creator = "select distinct catalogNumber, catalogName from catalogs;"
        results = self.database.select_data(get_creator)
        if results:
            return results, [result[0] for result in results]
        return None




