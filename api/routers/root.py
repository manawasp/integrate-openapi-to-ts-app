"""
routes.root
~~~~~~~~~~~~~~~~~~~~~~~

All routes related to root resources.
"""

from fastapi import APIRouter

router = APIRouter(
    tags=["default"],
)


@router.get("/", status_code=200, response_model=None, include_in_schema=False)
def get_root():
    return None


@router.get("/healthz", status_code=200, response_model=None, include_in_schema=False)
def get_healthz():
    return "OK"
