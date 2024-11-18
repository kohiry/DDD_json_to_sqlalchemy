FROM python:3.12-slim

WORKDIR /api

COPY poetry/api/ ./

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY ./src /api/src
COPY ./env/.env /api/.env
