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
from variate.update_cache.catalog_cache import UpdateCatalogCache
from variate.update_cache.entry_cache import UpdateEntryCache

app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(seconds=2*60*60)
app.config.from_object(configration)

# engine = create_engine('mysql+mysqlconnector://%s:%s@%s:3306/%s' %
#                        (app.config['MYSQL_USER'], app.config['MYSQL_PASSWORD'],
#                         app.config['MYSQL_HOST'], app.config['MYSQL_DB']))
# DBSession = sessionmaker(bind=engine)
# mysql_session = DBSession()

db = MysqlConnection(host=app.config['MYSQL_HOST'], username=app.config['MYSQL_USER'],
                     password=app.config['MYSQL_PASSWORD'], database=app.config['MYSQL_DB'])
command = SqlCom(db)

redis_pool = redis.ConnectionPool(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'],
                                  password=app.config['REDIS_PWD'], decode_responses=True)
redis_connection = redis.Redis(connection_pool=redis_pool)
redis_operate = RedisOperation(redis_connection)

update_catalog_caches = UpdateCatalogCache(command, redis_operate)
update_entry_caches = UpdateEntryCache(command, redis_operate)
if not redis_operate.check_key_exist_or_empty(RedisKey.catalog_entities):
    update_catalog_caches.update_catalog_entity()
if not redis_operate.check_key_exist_or_empty(RedisKey.creators):
    update_entry_caches.update_all_entry_creator()


@app.route('/')
def show_entries():
    result = command.get_all_entry()
    entries = [dict(title=row[0], text=row[1], id=row[2]) for row in result]
    catalog_entities = redis_operate.get_json_value(RedisKey.catalog_entities)
    creators = redis_operate.get_json_value(RedisKey.creators)
    return render_template('show_entries.html', entries=entries, creators=creators, catalog_entities=catalog_entities)


@app.route('/search', methods=['POST'])
def filter_by_catalog_id():
    try:
        if not session.get('logged_in'):
            abort(401)
        catalog_entities = redis_operate.get_json_value(RedisKey.catalog_entities)
        catalog_code = [catalog['catalog_num'] for catalog in catalog_entities]
        creators = redis_operate.get_json_value(RedisKey.creators)
        search_condition = dict(title=request.form['title'], sort=request.form['sort'],
                                catalog=request.form['catalog'], create_by=request.form['creator'])
        if int(request.form['catalog']) not in catalog_code:
            print('catalog error')
            return redirect(url_for('show_entries'))
        else:
            result = command.get_filtered_entry(search_condition)
            entries = [dict(title=row[0], text=row[1], id=row[2]) for row in result] if result else []
            return render_template(
                'show_entries.html', entries=entries, creators=creators,
                catalog_entities=catalog_entities, search_condition=search_condition)
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
        command.add_new_entry(title=request.form['title'], text=request.form['text'],
                              updateBy=username, Catalogs=int(request.form['catalog']))
        update_entry_caches.update_all_entry_creator()
        flash('New entry was successfully posted')
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
    command.update_entry(title=request.form['title'], text=request.form['text'],
                         updateBy=username, Catalogs=int(request.form['catalog']), id=int(request.form['id']))
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
        elif user_pwd != command.get_pwd(username):
            error = 'Invalid password'
        else:
            session.permanent = True
            session['logged_in'] = True
            session['username'] = username
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    try:
        if request.method == 'GET':
            return render_template('add_user.html', user_entity={})
        else:
            user_entity = dict(username1=request.form['username'], fullname=request.form['account'],
                               email=request.form['email'], password1=request.form['password'])
            if session.get('username') != 'admin':
                abort(403)
            if not request.form['username']:
                flash('username cannot be empty')
                return render_template('add_user.html', user_entity=user_entity)
            if command.check_username(request.form['username']):
                flash('user name already existed')
                return render_template('add_user.html', user_entity=user_entity)
            if not request.form['account']:
                flash('Full name cannot be empty')
                return render_template('add_user.html', user_entity=user_entity)
            if not request.form['email']:
                flash('email cannot be empty')
                return render_template('add_user.html', user_entity=user_entity)
            if not request.form['password']:
                flash('password cannot be empty')
                return render_template('add_user.html', user_entity=user_entity)
            if len(request.form['password']) < 8:
                flash('password length must great than 8')
                return render_template('add_user.html', user_entity=user_entity)
            md5pwd = hashlib.md5(request.form['password'].encode()).hexdigest()
            command.add_user(username=request.form['username'],
                             account=request.form['account'], pwd=md5pwd, email=request.form['email'])
            flash('add user %s success' % request.form['username'])
            return render_template('add_user.html', user_entity={})
    except Exception as user_error:
        print(user_error)
        return render_template('add_user.html', user_entity={})


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
