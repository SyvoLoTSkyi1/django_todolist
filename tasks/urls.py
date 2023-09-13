from django.contrib.auth import urls
from django.urls import path, include

from tasks.views import TaskView, TaskDetailView, CreateTaskView, UpdateTaskView, DeleteTaskView

urlpatterns = [
    path('task_list/', TaskView.as_view(), name='task_list'),
    path('task_list/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task-create/', CreateTaskView.as_view(), name='task-create'),
    path('task-update/<int:pk>/', UpdateTaskView.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteTaskView.as_view(), name='task-delete'),
]

