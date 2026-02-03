from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/health")
def health_check():
    """Endpoint 1: Health Check"""
    return {"status": "healthy", "environment": "staging", "version": os.getenv("APP_VERSION", "1.0.0")}

@app.post("/users")
def create_user(username: str, email: str):
    """Endpoint 2: User Creation (Interacts with database logic)"""
    return {"message": f"User {username} with email {email} created successfully in the staging database."}
