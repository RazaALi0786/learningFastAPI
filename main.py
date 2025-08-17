from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
import models
from sqlalchemy.orm import Session
from database import engine, get_db
from schemas import Post, PostCreate, UserCreate, UserOut
import utils
from routers import post, user, auth
models.Base.metadata.create_all(bind=engine)
app = FastAPI()


try:
    conn = psycopg2.connect(host='localhost', database='fastapi',
                            user='postgres', password='R@zaali1', cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print("Database connection successful")
except Exception as e:
    print("Database connection failed")
    print(f"Error: {e}")
    time.sleep(2)


my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "title of post 2", "content": "content of post 2", "id": 2}]


def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i
    return None


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
async def read_root():
    return {"message": "Black, World!"}
