from fastapi import FastAPI, HTTPException
from schemas import PostCreate, PostResponse
from db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

text_posts={
    1: {"title": "New Post", "content": "Cool"},
    2: {"title": "Update", "content": "Working on something big."},
    3: {"title": "Travel Log", "content": "Just landed in Tokyo!"},
    4: {"title": "Quick Thought", "content": "Consistency beats intensity."},
    5: {"title": "Photo Dump", "content": "Weekend highlights."},
    6: {"title": "Announcement", "content": "The shop is officially open."},
    7: {"title": "Review", "content": "5 stars. Would recommend."},
    8: {"title": "Question", "content": "What's everyone reading lately?"},
    9: {"title": "Coding Tip", "content": "Don't forget to comment your logic."},
    10: {"title": "Fitness", "content": "New personal best today!"},
    11: {"title": "Recipe", "content": "Simple 5-minute pasta."},
    12: {"title": "Reminder", "content": "Drink more water."},
    13: {"title": "Tech News", "content": "The new update is finally here."},
    14: {"title": "Mood", "content": "Feeling inspired."},
    15: {"title": "Throwback", "content": "Missing the summer heat."},
    16: {"title": "Project Alpha", "content": "First milestone reached."},
    17: {"title": "Life Update", "content": "We moved!"},
    18: {"title": "Gaming", "content": "Finally finished the final boss."},
    19: {"title": "Music", "content": "This album is on repeat."},
    20: {"title": "Draft", "content": "More details coming soon."},
}

@app.get("/posts")
def get_all_posts():
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int) -> PostResponse:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Page not found")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post
