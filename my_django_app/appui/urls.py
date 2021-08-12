from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("home", views.home, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contactus", views.contactus, name='contactus'),
]
