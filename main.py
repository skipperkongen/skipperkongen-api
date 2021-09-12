import os

from fastapi import FastAPI
import redis

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, world 2!"}

@app.get("/redis-counter/")
def redis_counter():
    """
    https://devcenter.heroku.com/articles/heroku-redis#connecting-in-python
    """
    r = redis.from_url(os.environ.get("REDIS_URL"))
    value = r.incr('redis_counter')
    return {"redis_counter": int(value)}
