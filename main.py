# importing fastapi library
from fastapi import FastAPI

# setting up the app to use the FastAPI framework
app = FastAPI()

# using the @app.get decorator to define the endpoint 
@app.get("/")
async def read_root():
    return {"Hello": "World"}


# added the @app.post  decorator to define the endpoint  to get posts items.
@app.get("/items/{item_id}")
def get_post_items():
    posts = [
        {
            "id": 1,
            "title": "First Post",
            "body": "This is the first post"
        },
        {
            "id": 2,
            "title": "Second Post",
            "body": "This is the second post"
        },
        {
            "id": 3,
            "title": "Third Post",
            "body": "This is the third post"
        }
    ]
    return posts