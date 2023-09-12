from django.contrib.auth import urls
from django.urls import path, include

from tasks.views import TaskView, TaskDetail

urlpatterns = [
    path('task_list/', TaskView.as_view(), name='task_list'),
    path('task_detail/', TaskDetail.as_view(), name='task_detail'),
]

