from django.conf.urls import url
from . import views

app_name='testApp'
urlpatterns = [
    url(r'^$', views.index,name='details'),
    url(r'^(?P<movie_id>[0-9]+)/$', views.getDetailsOfMovie, name='getDetails'),
    url(r'^favourite/$', views.favourite, name='favourite'),
]
