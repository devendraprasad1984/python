from django.urls import path
from geektrust.loan_payments.loan_manager import views

urlpatterns = [
    path('loan', views.fn_LOAN),
    path('payment', views.fn_PAYMENT),
    path('balance', views.fn_BALANCE),
]
