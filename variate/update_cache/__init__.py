from variate.redis_operation.redis_get_set import RedisOperation
from variate.sql_content.base_database import db


class BasicUpdateCache(object):

    def __int__(self, redis_con: RedisOperation):
        self.database = db
        self.redis_con = redis_con

    def update_cache(self):
        pass
