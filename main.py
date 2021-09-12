from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, world 2!"}

@app.get("/redis-counter/")
def redis_counter():
    r = redis.from_url(os.environ.get("REDIS_URL"))
    value = r.incr('redis_counter')
    return {"redis_counter": int(value)}
