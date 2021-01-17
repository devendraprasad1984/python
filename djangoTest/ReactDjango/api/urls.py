from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSets

router=routers.DefaultRouter()
router.register('users',UserViewSets)

urlpatterns = [
    path('',  include(router.urls)),
]
