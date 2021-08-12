from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns=[
    url(r'/dataset1/(?P<id>[0-9]+)/$',view=views.get_history_data)
]
