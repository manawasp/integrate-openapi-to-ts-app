import json

from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.openapi.utils import get_openapi

from main import app


def use_route_names_as_operation_ids(app: FastAPI) -> None:
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name.replace(" ", "_")


use_route_names_as_operation_ids(app)

print("Creating openapi.json file...")
with open("openapi.json", "w") as openapi_file:
    openapi_schema = get_openapi(
        title="My App",
        version="0.0.1",
        description="This is a very random API",
        routes=app.routes,
    )
    json.dump(openapi_schema, openapi_file)
print("openapi.json file generated")
