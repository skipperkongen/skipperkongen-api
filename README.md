# skipperkongen-api
An API

Run local:

```
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

## Using this deploy method

> https://youtu.be/H7zAJf20Moc

It's simple. Just commit and push to `main`. Then the API will be deployed to
Heroku via a web hook.
