from flask import jsonify, Blueprint, session, abort, request

from variate.redis_operation.redis_get_set import Redis
from variate.redis_operation.redis_key import RedisKey
from variate import db
from variate.sql_content.tables.tables_define import Catalogs

catalog_manage_opt = Blueprint('catalog_manage_opt', __name__)


@catalog_manage_opt.route('/query', methods=['GET'])
def query_catalog():
    pass


@catalog_manage_opt.route('/query/<catalog_id>', methods=['GET'])
def query_catalog():
    pass


@catalog_manage_opt.route('/add_catalog', methods=['POST'])
def add_catalog():
    # try:
    #     if not request.form['catalogName']:
    #         return jsonify({"error": "catalog name cannot be empty", "code": "10000"})
    #     max_catalog_namber = Catalogs.query(id).filter_by().first()
    #     command.add_new_catalog(catalog_name=request.form['catalogName'],
    #                             catalog_number=max_catalog_namber + 1, username=session.get('username'))
    #     update_catalog_caches.update_catalog_entity()
    #     flash('add catalog %s success' % request.form['catalogName'])
    #     return redirect(url_for('add_new_catalog_page'))
    # except Exception as some_error:
    #     print(some_error)
    #     return redirect(url_for('add_new_catalog_page'))
    pass
