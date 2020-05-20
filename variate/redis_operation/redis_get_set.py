import redis
import json


class RedisOperation(object):
    def __init__(self, conn: redis.Redis):
        self.conn = conn

    def set_key(self, name: str, value: str):
        return self.conn.set(name, value.replace('\'', '\"'))

    def get_json_value(self, name: str):
        return json.loads(self.conn.get(name))

    def get_str_value(self, name: str):
        return self.conn.get(name)

    def check_key_exist_or_empty(self, key: str):
        if not self.conn.exists(key):
            return False
        else:
            if not self.conn.get(key):
                return False
        return True
