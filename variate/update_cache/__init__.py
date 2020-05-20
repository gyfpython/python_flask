from variate.redis_operation.redis_get_set import RedisOperation
from variate.sql_content.sql_commond import SqlCom


class BasicUpdateCache(object):

    def __int__(self, database: SqlCom, redis_con: RedisOperation):
        self.database = database
        self.redis_con = redis_con

    def update_cache(self):
        pass
