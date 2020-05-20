import datetime
import hashlib

import redis
from flask import Flask, request, session, redirect, url_for, abort, \
    render_template, flash

from variate import configration
from variate.mysql_operation.mysql_connection import MysqlConnection
from variate.paras_assert.parameters_assert import check_username_valid
from variate.redis_operation.redis_get_set import RedisOperation
from variate.redis_operation.redis_key import RedisKey
from variate.sql_content.sql_commond import SqlCom
from variate.update_cache.catalog_cache import UpdateCatalogCache
from variate.update_cache.entry_cache import UpdateEntryCache

app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(seconds=2*60*60)
app.config.from_object(configration)

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
            return redirect(url_for('show_entries'))
        if int(request.form['catalog']) not in catalog_code:
            flash('catalog error')
            return redirect(url_for('show_entries'))
        username = session.get('username')
        command.add_new_entry(title=request.form['title'], text=request.form['text'],
                              updateBy=username, Catalogs=int(request.form['catalog']))
        update_entry_caches.update_all_entry_creator()
        flash('New entry was successfully posted')
        return redirect(url_for('show_entries'))
    except Exception as error:
        print(error)
        flash('error')
        return redirect(url_for('show_entries'))


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
