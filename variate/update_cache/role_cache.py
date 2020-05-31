from variate.redis_operation.redis_get_set import RedisOperation
from variate.redis_operation.redis_key import RedisKey
from variate.sql_content.sql_commond import SqlCom
from variate.update_cache import BasicUpdateCache


class UpdateRoleCache(BasicUpdateCache):
    def __init__(self, database: SqlCom, redis_con: RedisOperation):
        super().__int__(redis_con)
        self.database = database

    def update_role_cache(self):
        roles = self.database.get_all_role()
        if roles:
            roles_entities = [dict(role_name=row[0], role_code=row[1]) for row in roles]
        else:
            roles_entities = {}
        self.redis_con.set_key(RedisKey.role_entity, str(roles_entities))

    def add_user_role_cache(self, username: str):
        result = self.database.get_user_role(username)
        if result:
            user_role = dict(role_name=result[0][0], role_code=result[0][1])
        else:
            user_role = {}
        user_rule_key = username + RedisKey.user_role_post
        self.redis_con.set_key(user_rule_key, str(user_role))

