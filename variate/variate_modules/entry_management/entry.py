from flask import jsonify, Blueprint, session, abort, request

from variate.redis_operation.redis_get_set import Redis
from variate.redis_operation.redis_key import RedisKey
from variate import db
from variate.sql_content.tables.tables_define import Entry

entry_manage_opt = Blueprint('entry_manage_opt', __name__)


@entry_manage_opt.route('/add_entry', methods=['POST'])
def add_entry():
    pass