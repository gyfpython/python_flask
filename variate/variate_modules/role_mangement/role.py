from flask import jsonify, Blueprint, session, abort, request

from variate.redis_operation.redis_get_set import Redis
from variate.redis_operation.redis_key import RedisKey
from variate import db
from variate.sql_content.tables.tables_define import Roles, RolePermissions

role_manage_opt = Blueprint('role_manage_opt', __name__)


@role_manage_opt.route('/add_role', methods=['POST'])
def add_role():
    pass
