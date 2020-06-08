import datetime
import hashlib

import redis
from flask import Flask, request, session, redirect, url_for, abort, \
    render_template, flash

from variate import configration
from variate.sql_content.mysql_connection import MysqlConnection
from variate.paras_assert.parameters_assert import check_username_valid
from variate.redis_operation.redis_get_set import RedisOperation
from variate.redis_operation.redis_key import RedisKey
from variate.sql_content.sql_commond import SqlCom
from variate.sql_content.tables.tables_define import *
from variate.update_cache.catalog_cache import UpdateCatalogCache
from variate.update_cache.entry_cache import UpdateEntryCache
from variate.sql_content.base_database import db
from variate.update_cache.permission_cache import UpdatePermissionCache
from variate.update_cache.role_cache import UpdateRoleCache

app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(seconds=2*60*60)
app.config.from_object(configration)

with app.app_context():
    db.init_app(app)
    # db.create_all()

self_db = MysqlConnection(host=app.config['MYSQL_HOST'], username=app.config['MYSQL_USER'],
                     password=app.config['MYSQL_PASSWORD'], database=app.config['MYSQL_DB'])
command = SqlCom(self_db)

redis_pool = redis.ConnectionPool(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'],
                                  password=app.config['REDIS_PWD'], decode_responses=True)
redis_connection = redis.Redis(connection_pool=redis_pool)
redis_operate = RedisOperation(redis_connection)

update_catalog_caches = UpdateCatalogCache(command, redis_operate)
update_entry_caches = UpdateEntryCache(command, redis_operate)
update_role_cache = UpdateRoleCache(command, redis_operate)
update_permission_cache = UpdatePermissionCache(command, redis_operate)

update_catalog_caches.update_catalog_entity()
update_entry_caches.update_all_entry_creator()
update_role_cache.update_role_cache()
update_permission_cache.update_permission_cache()
update_permission_cache.update_all_role_permission()


def get_all_perm(username: str):
    role_name = redis_operate.get_json_value(username + RedisKey.user_role_post)['role_name']
    all_permissions = redis_operate.get_json_value(role_name + RedisKey.role_permission_post)
    permission_names = [permission['permission_name'] for permission in all_permissions]
    return permission_names


@app.route('/')
def show_entries():
    search_condition = dict(title='', sort='id',
                            catalog=-1, create_by='all')
    session['search_condition'] = search_condition
    all_entry = Entry.query.order_by('title').paginate(1, 10, error_out=False)
    catalog_entities = redis_operate.get_json_value(RedisKey.catalog_entities)
    if session.get('logged_in'):
        all_permissions = get_all_perm(session.get('username'))
    else:
        all_permissions = []
    creators = redis_operate.get_json_value(RedisKey.creators)
    return render_template('show_entries.html', pagination=all_entry, entries=all_entry.items,
                           creators=creators, catalog_entities=catalog_entities, all_permissions=all_permissions)


@app.route('/search', methods=['GET', 'POST'])
def filter_by_catalog_id():
    try:
        if not session.get('logged_in'):
            abort(401)
        page = request.args.get('page', 1, type=int)
        catalog_entities = redis_operate.get_json_value(RedisKey.catalog_entities)
        catalog_code = [catalog['catalog_num'] for catalog in catalog_entities]
        creators = redis_operate.get_json_value(RedisKey.creators)
        if request.method == 'POST':
            search_condition = dict(title=request.form['title'], sort=request.form['sort'],
                                    catalog=request.form['catalog'], create_by=request.form['creator'])
            session['search_condition'] = search_condition
            if int(request.form['catalog']) not in catalog_code and int(request.form['catalog']) != -1:
                print('catalog error')
                return redirect(url_for('show_entries'))
        else:
            search_condition = session.get('search_condition')
        if int(search_condition['catalog']) == -1 and search_condition['create_by'] == 'all':
            filter_entry = Entry.query.filter(
                Entry.title.like('%'+search_condition['title']+'%')) \
                .order_by(search_condition['sort']).paginate(page, 10, error_out=False)
        elif int(search_condition['catalog']) != -1 and search_condition['create_by'] == 'all':
            filter_entry = Entry.query.filter(
                Entry.Catalogs == int(search_condition['catalog']) and
                Entry.title.like('%'+search_condition['title']+'%')) \
                .order_by(search_condition['sort']).paginate(page, 10, error_out=False)
        elif int(search_condition['catalog']) == -1 and search_condition['create_by'] != 'all':
            filter_entry = Entry.query.filter(
                Entry.updateBy == search_condition['create_by'] and
                Entry.title.like('%'+search_condition['title']+'%')) \
                .order_by(search_condition['sort']).paginate(page, 10, error_out=False)
        else:
            filter_entry = Entry.query.filter(
                Entry.Catalogs == int(search_condition['catalog']) and
                Entry.updateBy == search_condition['create_by'] and
                Entry.title.like('%'+search_condition['title']+'%')) \
                .order_by(search_condition['sort']).paginate(page, 10, error_out=False)
        return render_template(
            'show_entries.html', entries=filter_entry.items, creators=creators, pagination=filter_entry,
            catalog_entities=catalog_entities, search_condition=search_condition,
            all_permissions=get_all_perm(session.get('username')))
    except Exception as error:
        print(error)
        return redirect(url_for('show_entries'))


@app.route('/add', methods=['POST'])
def add_entry():
    try:
        if not session.get('logged_in'):
            abort(401)
        catalog_entities = redis_operate.get_json_value(RedisKey.catalog_entities)
        catalog_code = [catalog['catalog_num'] for catalog in catalog_entities]
        if not request.form['title'] or not request.form['text']:
            flash('title or text cannot be empty')
            return redirect(url_for('add_new_entry'))
        if int(request.form['catalog']) not in catalog_code:
            flash('catalog error')
            return redirect(url_for('add_new_entry'))
        username = session.get('username')
        new_entry = Entry(title=request.form['title'], text=request.form['text'],
                          catalogs=int(request.form['catalog']), update_by=username)
        db.session.add(new_entry)
        db.session.commit()
        update_entry_caches.update_all_entry_creator()
        flash('New entry %s was successfully posted' % request.form['title'])
        return redirect(url_for('add_new_entry'))
    except Exception as error:
        print(error)
        flash('error')
        return redirect(url_for('add_new_entry'))


@app.route('/update', methods=['POST'])
def update_entry():
    if not session.get('logged_in'):
        abort(401)
    catalog_entities = redis_operate.get_json_value(RedisKey.catalog_entities)
    catalog_code = [catalog['catalog_num'] for catalog in catalog_entities]
    if int(request.form['catalog']) not in catalog_code:
        flash('catalog error')
        return redirect(url_for('show_entries'))
    if not request.form['title'] or not request.form['text']:
        flash('title or text cannot be empty')
        return redirect(url_for('show_entries'))
    username = session.get('username')
    update_a_entry = Entry.query.filter_by(id=int(request.form['id'])).first()
    update_a_entry.title = request.form['title']
    update_a_entry.Catalogs = int(request.form['catalog'])
    update_a_entry.text = request.form['text']
    update_a_entry.updateBy = username
    update_a_entry.createTime = datetime.datetime.now()
    db.session.commit()
    flash('entry %s was successfully updated' % request.form['title'])
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        user_pwd = hashlib.md5(request.form['password'].encode()).hexdigest()
        if not username or not check_username_valid(username):
            error = 'Invalid username'
        elif user_pwd != Users.query.filter_by(username=username).first().password:
            error = 'Invalid password'
        else:
            session.permanent = True
            session['logged_in'] = True
            session['username'] = username
            update_role_cache.add_user_role_cache(username)
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if not session.get('logged_in'):
        abort(401)
    all_permission = get_all_perm(session.get('username'))
    role_entities = redis_operate.get_json_value(RedisKey.role_entity)
    try:
        role_codes = [role['role_code'] for role in role_entities]
        if request.method == 'GET':
            return render_template('add_user.html', user_entity={}, role_entities=role_entities,
                                   all_permissions=all_permission)
        else:
            user_entity = dict(username1=request.form['username'], fullname=request.form['account'],
                               email=request.form['email'], password1=request.form['password'])
            if session.get('username') != 'admin':
                abort(403)
            if not request.form['username']:
                flash('username cannot be empty')
                return render_template('add_user.html', user_entity=user_entity,
                                       role_entities=role_entities, all_permissions=all_permission)
            if command.check_username(request.form['username']):
                flash('user name already existed')
                return render_template('add_user.html', user_entity=user_entity,
                                       role_entities=role_entities, all_permissions=all_permission)
            if not request.form['account']:
                flash('Full name cannot be empty')
                return render_template('add_user.html', user_entity=user_entity,
                                       role_entities=role_entities, all_permissions=all_permission)
            if not request.form['email']:
                flash('email cannot be empty')
                return render_template('add_user.html', user_entity=user_entity,
                                       role_entities=role_entities, all_permissions=all_permission)
            if not request.form['password']:
                flash('password cannot be empty')
                return render_template('add_user.html', user_entity=user_entity,
                                       role_entities=role_entities, all_permissions=all_permission)
            if not request.form['role'] or int(request.form['role']) not in role_codes:
                flash('must select a role')
                return render_template('add_user.html', user_entity=user_entity,
                                       role_entities=role_entities, all_permissions=all_permission)
            if len(request.form['password']) < 8:
                flash('password length must great than 8')
                return render_template('add_user.html', user_entity=user_entity,
                                       role_entities=role_entities, all_permissions=all_permission)
            md5pwd = hashlib.md5(request.form['password'].encode()).hexdigest()
            new_user = Users(username=request.form['username'], password=md5pwd,
                             account=request.form['account'], email=request.form['email'],
                             role_code=int(request.form['role']))
            db.session.add(new_user)
            db.session.commit()
            flash('add user %s success' % request.form['username'])
            return render_template('add_user.html', user_entity={},
                                   role_entities=role_entities, all_permissions=all_permission)
    except Exception as user_error:
        print(user_error)
        return render_template('add_user.html', user_entity={},
                               role_entities=role_entities, all_permissions=all_permission)


@app.route('/add_role', methods=['GET', 'POST'])
def add_role():
    if not session.get('logged_in'):
        abort(401)
        return redirect(url_for('show_entries'))
    whole_permissions = redis_operate.get_json_value(RedisKey.whole_permission)
    if request.method == 'GET':
        return render_template('add_role.html', whole_permissions=whole_permissions)
    elif request.method == 'POST':
        if not request.form['role_name']:
            flash('role name cannot be empty')
            return render_template('add_role.html', whole_permissions=whole_permissions)
        if not check_username_valid(request.form['role_name']):
            flash('role name cannot contain =, \', \", !, ;, %')
            return render_template('add_role.html', whole_permissions=whole_permissions)
        if Roles.query.filter_by(roleName=request.form['role_name']).first():
            flash('role name already existed')
            return render_template('add_role.html', whole_permissions=whole_permissions)
        if not request.form['description']:
            flash('description cannot be empty')
            return render_template('add_role.html', whole_permissions=whole_permissions)
        if not request.form['permissions']:
            flash('permissions cannot be empty')
            return render_template('add_role.html', whole_permissions=whole_permissions)
        new_permissions = request.form['permissions'].split(',')
        print(new_permissions)
        command.add_new_role(request.form['role_name'], request.form['description'], new_permissions)
        flash('create new role %s success ') % request.form['role_name']
        return render_template('add_role.html', whole_permissions=whole_permissions)
    else:
        return redirect(url_for('show_entries'))


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


@app.route('/edit_entry/<id>', methods=['GET'])
def edit_entry(id):
    try:
        catalog_entities = redis_operate.get_json_value(RedisKey.catalog_entities)
        check_exist, entry = command.check_entry_id_exist(int(id))
        if not check_exist:
            return redirect(url_for('show_entries'))
        else:
            return render_template('edit_entry.html', entry=entry[0], catalog_entities=catalog_entities)
    except Exception as id_error:
        print(id_error)
        return redirect(url_for('show_entries'))


@app.route('/add_entry', methods=['GET'])
def add_new_entry():
    try:
        catalog_entities = redis_operate.get_json_value(RedisKey.catalog_entities)
        return render_template('add_entry.html', catalog_entities=catalog_entities)
    except Exception as some_error:
        print(some_error)
        return redirect(url_for('show_entries'))


@app.route('/add_catalog_page', methods=['GET'])
def add_new_catalog_page():
    try:
        return render_template('add_catalog.html')
    except Exception as some_error:
        print(some_error)
        return redirect(url_for('add_new_catalog_page'))


@app.route('/add_catalog', methods=['POST'])
def add_catalog():
    try:
        if not request.form['catalogName']:
            flash('catalog name cannot be empty')
            return redirect(url_for('add_new_catalog_page'))
        max_catalog_namber = command.get_max_catalog_number()
        command.add_new_catalog(catalog_name=request.form['catalogName'],
                                catalog_number=max_catalog_namber+1, username=session.get('username'))
        update_catalog_caches.update_catalog_entity()
        flash('add catalog %s success' % request.form['catalogName'])
        return redirect(url_for('add_new_catalog_page'))
    except Exception as some_error:
        print(some_error)
        return redirect(url_for('add_new_catalog_page'))


@app.route('/delete_entry/<id>', methods=['GET'])
def delete_entry(id):
    try:
        check_exist, entry = command.check_entry_id_exist(int(id))
        if check_exist:
            command.delete_a_entry_by_id(int(id))
            update_entry_caches.update_all_entry_creator()
            flash('delete entry %s success' % entry[0]['title'])
        else:
            flash('entry %s not existed' % id)
    except Exception as id_error:
        print(id_error)
        flash('Error! Delete entry failed')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    app.run(port=8080)
