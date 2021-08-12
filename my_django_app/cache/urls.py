from django.conf.urls import url, include
from . import views

urlpatterns=[
    url(r'/mod1/(?P<id>[0-9]+)/$',view=views.get_mod1)
]
