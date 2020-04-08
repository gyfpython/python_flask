from flask import Flask
from file_operation.get_file_txt import get_text
app = Flask(__name__)


@app.route('/')
def index_page():
    return 'Index Page!'


@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/get_txt/<file_name>')
def get_txt(file_name):
    return get_text(file_name)


if __name__ == '__main__':
    app.run()
