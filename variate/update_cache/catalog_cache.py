from variate.redis_operation.redis_get_set import RedisOperation
from variate.redis_operation.redis_key import RedisKey
from variate.sql_content.sql_commond import SqlCom
from variate.update_cache import BasicUpdateCache


class UpdateCatalogCache(BasicUpdateCache):
    def __init__(self, database: SqlCom, redis_con: RedisOperation):
        super().__int__(database, redis_con)

    def update_catalog_entity(self):
        catalog_entity, catalog_code = self.database.get_all_catalog_code()
        if catalog_entity:
            catalog_entities = [dict(catalog_num=row[0], catalog_name=row[1]) for row in catalog_entity]
        else:
            catalog_entities = {}
        self.redis_con.set_key(RedisKey.catalog_entities, str(catalog_entities))