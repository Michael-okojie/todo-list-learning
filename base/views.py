from django.views.generic import ListView, DetailView
from .models import Task


class TaskList(ListView):
    models = Task
    context_object_name = 'tasks'
    queryset = Task.objects.all()


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'
    