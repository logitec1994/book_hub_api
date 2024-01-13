from fastapi import APIRouter
from .function import add_user, get_user, get_users, update_user, remove_user

router = APIRouter()

router.get("/users/{user_id}")(get_user)

# Get list of users (Not for reqular users) !! Check permitions
router.get("/users/")(get_users)

# Add new user to base
router.post("/users/")(add_user)

# # Update user by id
router.put("/users/{user_id}")(update_user)

# # Remove user by id
router.delete("/users/{user_id}")(remove_user)
