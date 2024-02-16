from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Task
from .forms import TaskForm

def task_list(request):
  tasks = Task.objects.all()
  return render(request, 'task_list.html', {'tasks' : tasks})

def create_task(request):
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/tasks')
  else:
    form = TaskForm()

  return render(request, 'create_task.html', {'form' : form})