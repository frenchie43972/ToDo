from .serializers import TaskSerializers
from .models import Task
from rest_framework import viewsets

# from .forms import TaskForm

# def task_list(request):
#   tasks = Task.objects.all()
#   return render(request, 'task_list.html', {'tasks' : tasks})

# def create_task(request):
#   if request.method == 'POST':
#     form = TaskForm(request.POST)
#     if form.is_valid():
#       form.save()
#       return HttpResponseRedirect('/tasks')
#   else:
#     form = TaskForm()

#   return render(request, 'create_task.html', {'form' : form})

class TaskViewSet(viewsets.ModelViewSet):
  queryset = Task.objects.all()
  serializer_class = TaskSerializers