from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.todo_list),
    path('view/', views.todo_list_view),
    path('insert_todo/', views.insert_todo_item, name='add_todo'),
    path('add_todo/<name>', views.add_todo),
    path('delete_todo/<int:todo_id>', views.delete_todo_item, name='del_todo')
]
