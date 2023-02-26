# importing fastapi library
from fastapi import FastAPI

# setting up the app to use the FastAPI framework
app = FastAPI()

# using the @app.get decorator to define the endpoint 
@app.get("/")
async def read_root():
    return {"Hello": "World"}
