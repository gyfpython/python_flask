import hashlib

from flask import jsonify, Blueprint, session, abort, request

from variate.redis_operation.redis_get_set import Redis
from variate.redis_operation.redis_key import RedisKey
from variate import db
from variate.sql_content.tables.tables_define import Users, UserRole

user_manage_opt = Blueprint('user_manage_opt', __name__)


@user_manage_opt.route('/query_users', methods=['GET'])
def query_users():
    if not session.get('username') == 'admin':
        abort(403)
    users = Users.query.filter().all()
    results = []
    for user in users:
        tem_user = user.__dict__
        del tem_user['_sa_instance_state']
        results.append(tem_user)
    return jsonify(results)


@user_manage_opt.route('/add_user', methods=['POST'])
def add_user():
    role_entities = Redis.read(RedisKey.role_entity)
    role_codes = [role['role_code'] for role in role_entities]
    # if session.get('username') != 'admin':
    #     abort(403)
    if not request.form['username']:
        return jsonify({'status': 'failed', 'code': -1, 'message': 'username cannot be empty'})
    if Users.query.filter(Users.username == request.form['username']).first():
        return jsonify({'status': 'failed', 'code': -1, 'message': 'user name already existed'})
    if not request.form['account']:
        return jsonify({'status': 'failed', 'code': -1, 'message': 'Full name cannot be empty'})
    if not request.form['email']:
        return jsonify({'status': 'failed', 'code': -1, 'message': 'email cannot be empty'})
    if not request.form['password']:
        return jsonify({'status': 'failed', 'code': -1, 'message': 'password cannot be empty'})
    if not request.form['role'] or int(request.form['role']) not in role_codes:
        return jsonify({'status': 'failed', 'code': -1, 'message': 'must select a role'})
    if len(request.form['password']) < 8:
        return jsonify({'status': 'failed', 'code': -1, 'message': 'password length must great than 8'})
    md5pwd = hashlib.md5(request.form['password'].encode()).hexdigest()
    new_user = Users(username=request.form['username'], password=md5pwd,
                     account=request.form['account'], email=request.form['email'],
                     role_code=int(request.form['role']))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'status': 'success', 'code': 1, 'message': 'add user success'})


