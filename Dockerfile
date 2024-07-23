FROM python:3.11.9-slim-bullseye
LABEL maintainer="patrykpawluk"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 5000

RUN apt-get -y update && \
    apt-get -y install build-essential && \
    apt-get -y install manpages-dev && \
    python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        flask-user

ENV PATH="/py/bin:$PATH"

USER flask-user
