from django.urls import path
from . import views

urlpatterns = [
    path('newtoken', views.fn_GET_NEW_TOKEN),
    path('subscribe', views.fn_SUBSCRIBE),
    path('list', views.gn_GET_SUBSCRIBERS),
]
