from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Black, World!"}

@app.get("/posts")
def get_posts():
    return {"data": "Here are your posts!"}