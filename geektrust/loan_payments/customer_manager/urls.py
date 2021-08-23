from django.urls import path

from . import views


urlpatterns = [
    path('addcustomer', views.fn_ADD_CUSTOMER),
    path('list', views.fn_GET_LIST_of_CUSTOMERS),
    path('list/<id>', views.fn_GET_LIST_of_CUSTOMERS),
    path('list/loan/ref/<loan_ref>', views.fn_GET_CUSTOMER_LOAN),
]
