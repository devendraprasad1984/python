from django.conf.urls import url
# from django.contrib import admin
from . import views

urlpatterns=[
    url(r'dataset1',view=views.get_history_data),
]
