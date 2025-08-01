from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
async def read_root():
    return {"message": "Black, World!"}

@app.get("/posts")
def get_posts():
    return {"data": "Here are your posts!"}

@app.post("/createposts")
def create_posts(post: Post):
    print(post.rating)
    print(post.dict())
    return {"new_post": "success"} 