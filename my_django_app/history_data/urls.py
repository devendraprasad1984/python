from django.conf.urls import url, include
# from django.contrib import admin
from . import views

urlpatterns=[
    url(r'dataset1',view=views.get_history_data),
    url(r'dataset2/<id>/$',view=views.get_history_data)
]
