from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

posts = [
    {
        "id": 1,
        "title": "Hello World",
        "content": "This is my first demo post.",
        "author": "Alice"
    },
    {
        "id": 2,
        "title": "FastAPI Tutorial",
        "content": "Learning how to build APIs with FastAPI.",
        "author": "Bob"
    },
    {
        "id": 3,
        "title": "Python Tips",
        "content": "Use list comprehensions for cleaner code.",
        "author": "Charlie"
    },
    {
        "id": 4,
        "title": "Database Design",
        "content": "Always normalize your database schema.",
        "author": "Diana"
    },
    {
        "id": 5,
        "title": "Travel Blog",
        "content": "I just visited Paris, it was amazing!",
        "author": "Eve"
    },
    {
        "id": 6,
        "title": "Cooking Recipe",
        "content": "Best pasta recipe with homemade sauce.",
        "author": "Frank"
    },
    {
        "id": 7,
        "title": "Book Review",
        "content": "1984 by George Orwell is a must-read.",
        "author": "Grace"
    },
    {
        "id": 8,
        "title": "Tech News",
        "content": "OpenAI just released a new AI model.",
        "author": "Henry"
    },
    {
        "id": 9,
        "title": "Sports Update",
        "content": "Real Madrid won their last game 3-1.",
        "author": "Ivy"
    },
    {
        "id": 10,
        "title": "Daily Motivation",
        "content": "Stay consistent, success will follow.",
        "author": "Jack"
    }
]


@app.get("/posts")
def get_posts(search: str | None = None):
    if search is None:
        return posts
    
    result = []
    for post in posts:
        if search.lower() in post['title'].lower() or search.lower() in post['content'].lower():
            result.append(post)

    return result

@app.get("/posts/{post_id}")
def get_one_post(post_id: int):
    for post in posts:
        if post['id'] == post_id:
            return post

@app.post("/posts")
def create_post(post: dict):
    posts.append(post)

@app.put("/posts/{post_id}")
def update_post(post_id: int, new_post_data: dict):
    for post in posts:
        if post['id'] == post_id:
            post.update(new_post_data)
            return

@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    for post in posts:
        if post['id'] == post_id:
            posts.remove(post)
            return