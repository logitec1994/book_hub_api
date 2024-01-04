import sqlite3

DB_NAME = "book.db"


def get_user_by_username(user_id):
    conn = sqlite3.connect(DB_NAME)
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
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        sql = "SELECT * FROM users"

        result = cur.execute(sql).fetchall()
        colums_names = [description[0] for description in cur.description]
        result_dict = [dict(zip(colums_names, row)) for row in result]

    if result:
        return result_dict

    return {"message": "Access denied"}


def add_new_user(username, email, password):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    sql = "INSERT INTO users(username, email, password_hash) VALUES(?, ?, ?)"
    try:
        cur.execute(sql, (username, email, password))
        conn.commit()
        conn.close()
    except sqlite3.IntegrityError:
        return {"message": "User already exists"}
    finally:
        conn.close()

    return {"message": "User successfully added"}
