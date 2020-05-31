from variate.redis_operation.redis_get_set import RedisOperation
from variate.redis_operation.redis_key import RedisKey
from variate.sql_content.sql_commond import SqlCom
from variate.update_cache import BasicUpdateCache


class UpdatePermissionCache(BasicUpdateCache):
    def __init__(self, database: SqlCom, redis_con: RedisOperation):
        super().__int__(redis_con)
        self.database = database

    def update_permission_cache(self):
        whole_permission = [permission for permission in self.get_whole_permission_tree()]
        self.redis_con.set_key(RedisKey.whole_permission, str(whole_permission))

    def get_whole_permission_tree(self):
        permissions = self.database.get_whole_permission_tree()
        if permissions:
            name = [dict(permission_name=permission_name[0], permission_code=permission_name[1])
                    for permission_name in permissions]
        else:
            name = []
        return name

    def update_all_role_permission(self):
        roles = self.database.get_all_role()
        for role in roles:
            result = self.database.get_rule_permission(role[1])
            if result:
                a_role_permission = [dict(permission_name=permission[0], permission_code=permission[1])
                                     for permission in self.database.get_rule_permission(role[1])]
            else:
                a_role_permission = []
            role_permission_key = role[0] + RedisKey.role_permission_post
            self.redis_con.set_key(role_permission_key, str(a_role_permission))

