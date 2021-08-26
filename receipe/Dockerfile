#https://hub.docker.com/_/python

FROM python:3.7-alpine
MAINTAINER DEVENDRAPRASAD1984@gmail.com

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt
RUN mkdir \app
WORKDIR /app
COPY ./app /app

#create user for running app in docker
RUN adduser -D dpadmin
USER dpadmin

