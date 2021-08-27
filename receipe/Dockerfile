#https://hub.docker.com/_/python
#docker build .
#docker-compose build
#docker-compose up -d --no-deps --build <service_name>
#docker-compose run app sh -c "django-admin.py startproject app ."
#docker-compose run app sh -c "django-admin.py startapp app ."
#docker-compose run app sh -c "python manage.py makemigrations"
#docker-compose run app sh -c "python manage.py migrate"
#docker-compose run app sh -c "python manage.py runserver 0.0.0.0:6204"
#docker-compose run app sh -c "python manage.py test && flake8"


FROM python:3.7-alpine
MAINTAINER DEVENDRAPRASAD1984@gmail.com

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt
RUN mkdir \app
WORKDIR /app
COPY ./app /app

#create user for running app in docker
#RUN adduser -D dpadmin
#USER dpadmin

