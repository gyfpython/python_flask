from flask import jsonify, Blueprint, session, abort, request

from variate.redis_operation.redis_get_set import Redis
from variate.redis_operation.redis_key import RedisKey
from variate import db
from variate.sql_content.tables.tables_define import Catalogs

catalog_manage_opt = Blueprint('catalog_manage_opt', __name__)


@catalog_manage_opt.route('query', methods=['GET'])
def query_catalog():
    pass


@catalog_manage_opt.route('/add_catalog', methods=['POST'])
def add_catalog():
    pass
