from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . import views
from . import todoView

router=routers.DefaultRouter()
router.register('users',views.UserViewSets)
router.register('books',views.BookViewSets)
router.register('tasks',views.TaskViewSets)

urlpatterns = [
    path('',  include(router.urls)),
]

# path('', todoView.apiOverview, name="api-overview"),
# path('task-list/', todoView.taskList, name="task-list"),
# path('task-detail/<str:pk>/', todoView.taskDetail, name="task-detail"),
# path('task-create/', todoView.taskCreate, name="task-create"),
# path('task-update/<str:pk>/', todoView.taskUpdate, name="task-update"),
# path('task-delete/<str:pk>/', todoView.taskDelete, name="task-delete"),

