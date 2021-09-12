# skipperkongen-api
An API

Run local:

```
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

View online:

```
curl https://skipperkongen.herokuapp.com/
```

## Heroku stuff

First:

```
heroku login
```

View CLI:

```
heroku logs -a skipperkongen
```

## Deploying

> https://youtu.be/H7zAJf20Moc

It's simple. Just commit and push to `main`. Then the API will be deployed to
Heroku via a web hook.
