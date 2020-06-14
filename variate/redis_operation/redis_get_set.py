import json
from flask import current_app
import redis


class Redis(object):
    """
    redis数据库操作
    """

    @staticmethod
    def _get_r():
        host = current_app.config['REDIS_HOST']
        port = current_app.config['REDIS_PORT']
        pwd = current_app.config['REDIS_PASSWORD']
        r = redis.StrictRedis(host=host, port=port, password=pwd)
        return r

    @classmethod
    def write(cls, key, value, expire=None):
        """
        写入键值对
        """
        # 判断是否有过期时间，没有就设置默认值
        if expire:
            expire_in_seconds = expire
        else:
            expire_in_seconds = current_app.config['REDIS_EXPIRE']
        r = cls._get_r()
        r.set(key, value, ex=expire_in_seconds)

    @classmethod
    def read(cls, key):
        """
        读取键值对内容
        """
        r = cls._get_r()
        value = json.loads(r.get(key))
        return value

    @classmethod
    def hset(cls, name, key, value):
        """
        写入hash表
        """
        r = cls._get_r()
        r.hset(name, key, value)

    @classmethod
    def hmset(cls, key, *value):
        """
        读取指定hash表的所有给定字段的值
        """
        r = cls._get_r()
        value = r.hmset(key, *value)
        return value

    @classmethod
    def hget(cls, name, key):
        """
        读取指定hash表的键值
        """
        r = cls._get_r()
        value = r.hget(name, key)
        return value.decode('utf-8') if value else value

    @classmethod
    def hgetall(cls, name):
        """
        获取指定hash表所有的值
        """
        r = cls._get_r()
        return r.hgetall(name)

    @classmethod
    def delete(cls, *names):
        """
        删除一个或者多个
        """
        r = cls._get_r()
        r.delete(*names)

    @classmethod
    def hdel(cls, name, key):
        """
        删除指定hash表的键值
        """
        r = cls._get_r()
        r.hdel(name, key)

    @classmethod
    def expire(cls, name, expire=None):
        """
        设置过期时间
        """
        if expire:
            expire_in_seconds = expire
        else:
            expire_in_seconds = current_app.config['REDIS_EXPIRE']
        r = cls._get_r()
        r.expire(name, expire_in_seconds)


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
