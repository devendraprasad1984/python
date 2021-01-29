from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.todo_list),
    path('view/',views.todo_list_view)
]
