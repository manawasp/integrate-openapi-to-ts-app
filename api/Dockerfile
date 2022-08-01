# syntax=docker/dockerfile:1.0.0-experimental
###############################################################################

FROM python:3.10.6-slim as build

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY main.py main.py
COPY routers routers

EXPOSE 8000

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]
