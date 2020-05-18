import hashlib
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
import redis
from sqlalchemy import create_engine

from flaskr import configration
from flaskr.mysql_operation.mysql_connection import MysqlConnection
from flaskr.paras_assert.check_entry_exist import check_entry_id_exist
from flaskr.paras_assert.parameters_assert import check_username_valid
from flaskr.redis_operation.redis_key import RedisKey
from flaskr.redis_operation.redis_get_set import RedisOperation
from flaskr.sql_content.sql_commond import SqlCom
import datetime


app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(seconds=2*60*60)
app.config.from_object(configration)

# engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1:3306/flask')
db = MysqlConnection(host=app.config['MYSQL_HOST'], username=app.config['MYSQL_USER'],
                     password=app.config['MYSQL_PASSWORD'], database=app.config['MYSQL_DB'])
command = SqlCom(db)
creators = command.get_all_entry_creator()
catalog_entity, catalog_code = command.get_all_catalog_code()
if catalog_entity:
    catalog_entities = [dict(catalog_num=row[0], catalog_name=row[1]) for row in catalog_entity]
else:
    catalog_entities = {}

global redis_operate
redis_pool = redis.ConnectionPool(
    host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'],
    password=app.config['REDIS_PWD'], decode_responses=True)
redis_connection = redis.Redis(connection_pool=redis_pool)
redis_operate = RedisOperation(redis_connection)
redis_operate.set_key(RedisKey.creators, str(creators))
redis_operate.set_key(RedisKey.catalog_entities, str(catalog_entities))


@app.route('/')
def show_entries():
    result = command.get_all_entry()
    entries = [dict(title=row[0], text=row[1], id=row[2]) for row in result]
    catalogs = redis_operate.get_json_value(RedisKey.catalog_entities)
    cache_creators = redis_operate.get_json_value(RedisKey.creators)
    return render_template('show_entries.html', entries=entries, creators=cache_creators, catalog_entities=catalogs)


@app.route('/search', methods=['POST'])
def filter_by_catalog_id():
    try:
        if not session.get('logged_in'):
            abort(401)
        search_condition = dict(title=request.form['title'], sort=request.form['sort'],
                                catalog=request.form['catalog'], create_by=request.form['creator'])
        if int(request.form['catalog']) not in catalog_code:
            print('catalog error')
            return redirect(url_for('show_entries'))
        else:
            result = command.get_filtered_entry(search_condition)
            entries = [dict(title=row[0], text=row[1], id=row[2]) for row in result]
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
        if not request.form['title'] or not request.form['text']:
            flash('title or text cannot be empty')
            return redirect(url_for('show_entries'))
        if int(request.form['catalog']) not in catalog_code:
            flash('catalog error')
            return redirect(url_for('show_entries'))
        username = session.get('username')
        sql = "insert into entries (title, text, updateBy, createTime, Catalogs) " \
              "values ('{title}', '{text}', '{user}', '{datetime}', '{catalogs}')"
        sql1 = sql.format(title=request.form['title'], text=request.form['text'],
                          user=username, datetime=datetime.datetime.now(), catalogs=int(request.form['catalog']))
        db.connect_db(sql1)
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
    if not request.form['title'] or not request.form['text']:
        flash('title or text cannot be empty')
        return redirect(url_for('show_entries'))
    username = session.get('username')
    sql = "update entries set title='{title}', text='{text}', updateBy='{user}', createTime='{datetime}' " \
          "where id = {id}"
    sql1 = sql.format(title=request.form['title'], text=request.form['text'],
                      user=username, datetime=datetime.datetime.now(), id=request.form['id'])
    db.connect_db(sql1)
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
        check_exist, entry = check_entry_id_exist(db, id)
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
        check_exist, entry = check_entry_id_exist(db, id)
        if check_exist:
            delete_entry_sql = "delete from entries where id = {id}".format(id=int(id))
            db.connect_db(delete_entry_sql)
            flash('delete entry %s success' % entry[0]['title'])
        else:
            flash('entry %s not existed' % id)
    except Exception as id_error:
        print(id_error)
        flash('Error! Delete entry failed')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    app.run(port=8080)
