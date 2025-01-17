from db import db

# Use the db variable for database operations
users_collection = db.get_collection("users")
# ... perform operations on users_collection ...
