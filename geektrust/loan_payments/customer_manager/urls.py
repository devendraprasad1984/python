from django.urls import path
from . import views

urlpatterns = [
    path('addcustomer', views.fn_ADD_CUSTOMER),
]
