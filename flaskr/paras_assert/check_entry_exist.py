from flaskr.mysql_operation.mysql_connection import MysqlConnection


def check_entry_id_exist(db: MysqlConnection, id_int):
    try:
        int_id = int(id_int)
        select_by_id = "select title, text, id, Catalogs from entries where id = {id}".format(id=int_id)
        result = db.select_data(select_by_id)
        print(select_by_id)
        entry = [dict(title=row[0], text=row[1], id=row[2], catalogs=row[3]) for row in result]
        if not entry or len(entry) > 1:
            return False, None
        else:
            entry[0]['text'] = entry[0]['text'].replace('\r\n', '')
            return True, entry
    except Exception as id_error:
        print(id_error)
        return False, None
