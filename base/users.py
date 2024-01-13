import dataset
from fastapi.responses import JSONResponse

DB_NAME = "sqlite:///book.db"

# Create


def create_user(username, email, password):
    db = dataset.connect(DB_NAME)
    is_exists = get_user(username, email)

    if is_exists:
        return JSONResponse(content={"message": "User already exist"}, status_code=406)

    if not is_exists:
        db = dataset.connect(url=DB_NAME)
        table = db["users"]
        table.insert(
            dict(username=username, email=email, password_hash=password)
        )
        return JSONResponse(
            content={"message": "User successfully added"}, status_code=201
        )

    return JSONResponse(content={"message": "Unexpected error"}, status_code=418)


# Read


def get_user(username=None, email=None):
    if username is None and email is None:
        return JSONResponse(content={"message": "Need to send at least one argument"}, status_code=418)
    db = dataset.connect(url=DB_NAME)
    table = db["users"]
    result = table.find_one(username=username)
    if result:
        return result

    result = table.find_one(email=email)
    if result:
        return result

    return None


def get_users():
    db = dataset.connect(url=DB_NAME)
    table = db['users']
    result = table.find()
    print(list(result))

# Update


def update_user():
    ...

# Delete


def remove_user():
    ...
