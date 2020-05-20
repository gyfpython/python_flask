import pymysql


class MysqlConnection(object):
    def __init__(
            self, host: str = None, port: int = 3306, username: str = None, password: str = None, database: str = None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database

    def create_db(self):
        pass

    def connect_db(self, command: str):
        if not command:
            assert "command or database error"
        database = pymysql.connect(
            host=self.host, port=self.port, user=self.username, password=self.password, database=self.database)
        cursor = database.cursor()
        cursor.execute(command)
        database.commit()
        database.close()

    def select_data(self, command: str):
        if not command:
            assert "command or database error"
        database = pymysql.connect(
            host=self.host, port=self.port, user=self.username, password=self.password, database=self.database)
        cursor = database.cursor()
        cursor.execute(command)
        results = cursor.fetchall()
        database.close()
        return list(results)

    def create_table(self, table_name):
        pass

    def insert_raw(self, command: str):
        self.connect_db(command)

    def delete_raw(self):
        pass

