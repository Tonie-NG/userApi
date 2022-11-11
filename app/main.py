from fastapi import FastAPI, Path, Query
from typing import Optional, List
from pydantic import BaseModel

app = FastAPI()

users = ["okay"]

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users", response_model=List[User])
def get_users():
    return users

@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"

@app.get("/users/{id}")
async def get_user(
    id: int = Path(..., description="The ID of the user you want to retrieve"), 
    q: str = Query(None, max_length = 5)
):
    return {"user": users[id], "query": q }