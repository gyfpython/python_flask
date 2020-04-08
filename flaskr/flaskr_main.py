# all the imports
import hashlib
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
from flaskr import configration
from flaskr.mysql_operation.mysql_connection import MysqlConnection

app = Flask(__name__)
app.config.from_object(configration)


db = MysqlConnection(host='127.0.0.1', username='root', password='root', database='flask')


@app.route('/')
def show_entries():
    result = db.select_data("select title, text from entries order by id desc")
    # cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in result]
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    print(request.form['title'], request.form['text'])
    sql = "insert into entries (title, text, updateBy) values ('{title}', '{text}', '{user}')"
    sql1 = sql.format(title=request.form['title'], text=request.form['text'], user=app.config['USERNAME'])
    db.connect_db(sql1)
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user_pwd = hashlib.md5(request.form['password'].encode()).hexdigest()
        print(user_pwd)
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif user_pwd != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


@app.route('/get_all_rows')
def get_all_rows():
    result = db.select_data("SELECT value FROM test_table")
    results = []
    for raw in result:
        results.append(raw[0])
    return '/'.join(results)


if __name__ == '__main__':
    app.run(port=8080)
