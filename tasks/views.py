from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from tasks.model_forms import TaskModelForm
from tasks.models import Task


class TaskView(ListView):
    model = Task


class TaskDetailView(DetailView):
    model = Task


class CreateTaskView(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task_list')


class UpdateTaskView(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task_list')


class DeleteTaskView(DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')
