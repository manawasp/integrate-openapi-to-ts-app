# API

This api is built using [FastAPI](https://fastapi.tiangolo.com/) and handle two resources: Recipes & RecipesComments. Behind the api does nothing and returns static response.

## Summary
- [API](#api)
  - [Summary](#summary)
  - [Run locally](#run-locally)
  - [Available endpoints](#available-endpoints)

## Run locally

```sh
$ python3.10 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt -r requirements-tests.txt
(venv) $ uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['integrate-openapi-to-ts-app/api']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [170135] using StatReload
INFO:     Started server process [170137]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

We can now play with the running API

```sh
➜ curl http://127.0.0.1:8000/recipes | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   110  100   110    0     0  15356      0 --:--:-- --:--:-- --:--:-- 15714
{
  "meta": {
    "total": 2
  },
  "recipes": [
    {
      "id": 1,
      "name": "Bavarois aux fraises"
    },
    {
      "id": 2,
      "name": "Clafoutis aux poires"
    }
  ]
}
```

## Available endpoints

```
# Recipes resource
[GET] /recipes
[POST] /recipes
[GET] /recipes/{recipeId}
[PATCH] /recipes/{recipeId}
[DELETE] /recipes/{recipeId}

# RecipesComments resource
[GET] /recipes/{recipeId}/comments
[POST] /recipes/{recipeId}/comments
[GET] /recipes/{recipeId}/comments/{commentId}
[UPDATE] /recipes/{recipeId}/comments/{commentId}
[DELETE] /recipes/{recipeId}/comments/{commentId}

# Statically generate errors
[GET] /not_found
[GET] /unauthorized
```
