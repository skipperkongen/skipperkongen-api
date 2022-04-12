# skipperkongen-api
An API

View online:

```
curl https://skipperkongen.herokuapp.com/
```

View logs:

```
heroku logs --tail --app skipperkongen
```

## Run locally

Start server:

```
uvicorn main:app --reload
```

Authorize johndoe:
```bash
curl -d 'grant_type=password&username=johndoe&password=secret' localhost:8000/token
# OR
curl -d 'grant_type=password&username=alice&password=secret2' localhost:8000/token

# Returns a Token...
```

Get secured resource:

```bash
  curl localhost:8000/users/me/items/ -H 'Authorization: Bearer TOKEN_FROM_ABOVE'
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
