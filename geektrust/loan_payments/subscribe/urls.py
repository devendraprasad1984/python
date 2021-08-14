from django.urls import path
from . import views

urlpatterns = [
    path('newtoken', views.fn_GET_NEW_TOKEN),
    path('apisigner', views.fn_CHECK_API_SIGNER),
    path('subscribe', views.fn_SUBSCRIBE),
    path('subscription_list', views.gn_GET_SUBSCRIBERS),
]
