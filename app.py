from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    email: str

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/users")
def create_user(user: User):
    return {"message": f"User {user.username} created successfully."}
