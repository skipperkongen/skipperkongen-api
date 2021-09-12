import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import redis


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# Using template
## https://fastapi.tiangolo.com/advanced/templates/

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/redis-counter/")
def redis_counter():
    """
    https://devcenter.heroku.com/articles/heroku-redis#connecting-in-python
    """
    r = redis.from_url(os.environ.get("REDIS_URL"))
    value = r.incr('redis_counter')
    return {"redis_counter": int(value)}
