FROM python:3.12-slim

WORKDIR /migrations

COPY ./poetry/migrations ./
COPY ./alembic.ini ./

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY ./src/domain/models /migrations/src/domain/models
COPY ./src/infrastructure/database/base.py /migrations/src/infrastructure/database/base.py
COPY ./src/core /migrations/src/core
COPY ./env/.env /migrations/.env
