import sqlite3


def get_user_by_username(user_id):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    sql = "SELECT * FROM users WHERE username = ?"
    result = cur.execute(sql, (user_id,)).fetchone()

    if result:
        return result

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

    if result:
        return result

    return {"message": "Users not found"}
