from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import asyncpg
import os

app = FastAPI()

# Конфигурация
DATABASE_URL = os.getenv("DATABASE_URL")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: str
    password: str

@app.post("/register")
async def register(user: User):
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        await conn.execute(
            "INSERT INTO users (username, email, password) VALUES ($1, $2, $3)",
            user.username, user.email, user.password
        )
        return {"message": "User created"}
    finally:
        await conn.close()
