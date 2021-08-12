from django.urls import path
from . import views

urlpatterns = [
    path('addbank', views.fn_ADD_BANK),
]
