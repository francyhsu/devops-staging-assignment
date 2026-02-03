from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the data model to match your test script
class UserSchema(BaseModel):
    username: str
    email: str

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/users")
def create_user(user: UserSchema):
    # This logic matches the 'successfully' requirement in your test
    return {"message": f"User {user.username} created successfully."}
