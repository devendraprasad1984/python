#https://hub.docker.com/_/python
#run project steps
#docker-compose run app sh -c "django-admin.py startproject app ."
#docker-compose run app sh -c "django-admin.py startapp app ."
#docker-compose run app sh -c "python manage.py runserver 0.0.0.0:6203"

FROM python:3.7-alpine
MAINTAINER DEVENDRAPRASAD1984@gmail.com

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt
RUN mkdir /app
WORKDIR /app
COPY ./ /app

#create user for running app in docker
#RUN adduser -D dpadmin
#USER dpadmin

