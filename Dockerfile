# syntax=docker/dockerfile:1

FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /code
RUN apt-get update && apt-get -y install libpq-dev gcc

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

RUN touch .env
RUN echo "SENTRY_DSN=$SENTRY_DSN" > .env && echo "ENV=development" > .env && echo "SECRET_KEY=$SECRET_KEY" > .env

COPY . /code/

CMD python3 manage.py runserver 0.0.0.0:8000
