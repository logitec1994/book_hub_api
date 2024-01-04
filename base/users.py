import sqlite3


def get_user_by_username(user_id):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    sql = "SELECT * FROM users WHERE username = ?"
    result = cur.execute(sql, (user_id,)).fetchone()
    colums_names = [description[0] for description in cur.description]
    result_dict = dict(zip(colums_names, result))

    if result:
        return result_dict

    return {"message": "User not found"}


def get_users_list(permitions):
    result = ""
    if permitions == "user":
        return None

    if permitions == "admin":
        conn = sqlite3.connect("book.db")
        cur = conn.cursor()
        sql = "SELECT * FROM users"

        result = cur.execute(sql).fetchall()
        colums_names = [description[0] for description in cur.description]
        result_dict = [dict(zip(colums_names, row)) for row in result]

    if result:
        return result_dict

    return {"message": "Users not found"}


def add_new_user():
    ...
