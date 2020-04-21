from flaskr.mysql_operation.mysql_connection import MysqlConnection


class SqlCom(object):
    def __init__(self, database: MysqlConnection):
        self.database = database

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


db = MysqlConnection(host='127.0.0.1', username='root', password='root', database='flask')
SqlCom(db).check_username('test')
SqlCom(db).get_pwd('test')

