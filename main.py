from fastapi import FastAPI
from base.users import get_user_by_username, get_users_list, add_new_user


app = FastAPI()


# Get user by itself name
app.get("/users/{user_id}")(get_user_by_username)

# Get list of users (Not for reqular users) !! Check permitions
app.get("/users/")(get_users_list)

# Add new user to base
app.post("/users/")(add_new_user)
