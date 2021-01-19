from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . import views
from . import todoUrls
from website import webroutes

router = routers.DefaultRouter()
router.register('users', views.UserViewSets)
router.register('books', views.BookViewSets)

urlpatterns = []
appRoutes=[todoUrls.routes, webroutes.routes]

urlpatterns.append(path('', include(router.urls)))
for route in appRoutes:
    for x in route:
        urlpatterns.append(path(x[0], x[1]))
