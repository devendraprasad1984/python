from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . import views
from . import todoUrls

router=routers.DefaultRouter()
router.register('users',views.UserViewSets)
router.register('books',views.BookViewSets)
# router.register('tasks',views.TaskViewSets)
urlpatterns=[]
appRoutes=[todoUrls.routes] #provides custom routes for different parts of apps like so

urlpatterns.append(path('',  include(router.urls)))
for route in appRoutes:
    for x in route:
        urlpatterns.append(path(x[0],x[1]))

# , name="task-delete"
