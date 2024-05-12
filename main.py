from fastapi import FastAPI, HTTPException
from.database import Database
from.models import Post, Comment

app = FastAPI()
db = Database()

@app.post("/posts/")
async def create_post(post: Post):
    collection = await db.get_collection("posts")
    result = await collection.insert_one(post.dict())
    new_post = await collection.find_one({"_id": result.inserted_id})
    return new_post

@app.get("/posts/{post_id}")
async def read_post(post_id: str):
    collection = await db.get_collection("posts")
    post = await collection.find_one({"_id": post_id})
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.put("/posts/{post_id}")
async def update_post(post_id: str, post: Post):
    collection = await db.get_collection("posts")
    result = await collection.update_one({"_id": post_id}, {"$set": post.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"status": "success"}

@app.delete("/posts/{post_id}")
async def delete_post(post_id: str):
    collection = await db.get_collection("posts")
    result = await collection.delete_one({"_id": post_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"status": "success"}

# Implement similar endpoints for comments
