from flaskr.redis_operation.redis_get_set import RedisOperation
from flaskr.redis_operation.redis_key import RedisKey
from flaskr.sql_content.sql_commond import SqlCom
from flaskr.update_cache import BasicUpdateCache


class UpdateEntryCache(BasicUpdateCache):

    def __init__(self, database: SqlCom, redis_con: RedisOperation):
        super().__int__(database, redis_con)

    def update_all_entry_creator(self):
        creators = self.database.get_all_entry_creator()
        self.redis_con.set_key(RedisKey.creators, str(creators))
