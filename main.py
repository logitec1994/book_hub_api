from fastapi import FastAPI
from app.modules.users.endpoints import router

app = FastAPI()
app.include_router(router)


# ####

# # Get user by itself name
# app.get("/product/{prodict_id}")(get_product)

# # Get list of product (Not for reqular product) !! Check permitions
# app.get("/products/")(get_products)

# # Add new user to base
# app.post("/product/")(create_product)

# # Update user by id
# app.put("/product/{prodict_id}")(update_product)

# # Remove user by id
# app.delete("/product/{prodict_id}")(remove_product)

# # Product rating
# app.get("/product/{prodict_id}/rating")(get_product_rating)
