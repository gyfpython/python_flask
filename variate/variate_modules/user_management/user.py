from variate.sql_content.tables.tables_define import Users
from flask import jsonify, Blueprint

user_manage_opt = Blueprint('user_manage_opt', __name__)


@user_manage_opt.route('/query_users', methods=['GET'])
def query_users():
    users = Users.query.filter().all()
    results = []
    for user in users:
        tem_user = user.__dict__
        del tem_user['_sa_instance_state']
        results.append(tem_user)
    return jsonify(results)

