from fastapi import FastAPI

from routers import (
    recipes,
    recipes_comments,
    custom,
    root,
)

app = FastAPI()

app.include_router(root.router)
app.include_router(recipes.router)
app.include_router(recipes_comments.router)
app.include_router(custom.router)
