from flask import Flask, request, session, redirect, url_for, abort, render_template, flash, jsonify
import datetime

from variate.config import config
from variate.sql_content.base_database import db
from variate.variate_modules.catalog_management.catalog import catalog_manage_opt
from variate.variate_modules.entry_management.entry import entry_manage_opt
from variate.variate_modules.role_mangement.role import role_manage_opt
from variate.variate_modules.user_management.user import user_manage_opt


def create_app():
    app = Flask(__name__)
    app.permanent_session_lifetime = datetime.timedelta(seconds=2*60*60)
    app.config.from_object(config.config['Development'])
    app.register_blueprint(user_manage_opt, url_prefix="/user_manage_opt")
    app.register_blueprint(role_manage_opt, url_prefix="/role_manage_opt")
    app.register_blueprint(catalog_manage_opt, url_prefix="/catalog_manage_opt")
    app.register_blueprint(entry_manage_opt, url_prefix="/entry_manage_opt")
    with app.app_context():
        db.init_app(app)
    return app


# app = create_app()
#
#
# @app.route('/', methods=['GET'])
# def test1():
#     book = {'book': 'book'}
#     return jsonify(book)
#
#
# if __name__ == '__main__':
#     app.run(port=8080)


