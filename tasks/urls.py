from django.urls import path

from tasks.views import TaskView, TaskDetailView, CreateTaskView, \
    UpdateTaskView, DeleteTaskView, CreateCategoryView, \
    UpdateCategoryView, DeleteCategoryView

urlpatterns = [
    path('task_list/', TaskView.as_view(), name='task_list'),
    path('task_list/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task-create/', CreateTaskView.as_view(), name='task-create'),
    path('task-update/<int:pk>/', UpdateTaskView.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteTaskView.as_view(), name='task-delete'),
    path('category-create/', CreateCategoryView.as_view(), name='category-create'),
    path('category-update/<int:pk>/', UpdateCategoryView.as_view(), name='category-update'),
    path('category-delete/<int:pk>/', DeleteCategoryView.as_view(), name='category-delete'),
]
