from django.urls import path

from . import views


urlpatterns = [
    path('addbank', views.fn_ADD_BANK),
    path('list', views.fn_GET_LIST_of_BANKS),
]
