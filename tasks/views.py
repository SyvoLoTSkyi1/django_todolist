from django.shortcuts import render
from django.views.generic import ListView, DetailView

from tasks.models import Task


class TaskView(ListView):
    model = Task


class TaskDetail(DetailView):
    model = Task
