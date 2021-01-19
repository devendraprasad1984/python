from . import todoView
# from website import views

routes = [
    (r'task-views', todoView.apiOverview),
    (r'task-list/', todoView.taskList),
    (r'task-detail/<str:pk>/', todoView.taskDetail),
    (r'task-create/', todoView.taskCreate),
    (r'task-update/<str:pk>/', todoView.taskUpdate),
    (r'task-delete/<str:pk>/', todoView.taskDelete),
]

