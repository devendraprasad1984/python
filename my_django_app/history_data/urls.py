from django.urls import path
# from django.contrib import admin
from . import views

urlpatterns = [
    path("dataset1", views.get_history_data),
]
