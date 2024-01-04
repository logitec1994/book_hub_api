import sqlite3
from fastapi.responses import JSONResponse

DB_NAME = "book.db"


def get_user_by_username(user_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    sql = "SELECT * FROM users WHERE username = ?"
    result = cur.execute(sql, (user_id,)).fetchone()
    colums_names = [description[0] for description in cur.description]
    result_dict = dict(zip(colums_names, result))

    if result:
        return JSONResponse(content=result_dict, status_code=200)

    return JSONResponse(content={"message": "User not found"}, status_code=404)


def get_users_list(permitions):
    result = ""
    if permitions == "admin":
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        sql = "SELECT * FROM users"

        result = cur.execute(sql).fetchall()
        colums_names = [description[0] for description in cur.description]
        result_dict = [dict(zip(colums_names, row)) for row in result]

        if result:
            return JSONResponse(content=result_dict, status_code=200)

    return JSONResponse(content={"message": "Access denied"}, status_code=403)


def add_new_user(username, email, password, permitions):
    if permitions == "admin":
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        sql = "INSERT INTO users(username, email, password_hash) VALUES(?, ?, ?)"
        try:
            cur.execute(sql, (username, email, password))
            conn.commit()
            conn.close()
        except sqlite3.IntegrityError:
            return JSONResponse(content={"message": "User already exists"}, status_code=409)
        finally:
            conn.close()

        return JSONResponse(content={"message": "User successfully added"}, status_code=201)

    return JSONResponse(content={"message": "Access denied"}, status_code=403)
