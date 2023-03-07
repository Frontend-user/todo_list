from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import TaskModel
from django.http import HttpResponse


def index(request):
    return render(request, 'Api/index.html')

def tasks(request):
    return render(request, 'Api/tasks.html')

def false(request):
    return render(request, 'Api/false.html')

def task_create(request):
    if request.method == 'POST':
        task = TaskForm(request.POST)
        if task.is_valid():
            text = task.cleaned_data['text']
            TaskModel.objects.create(text=text)
            all_tasks = TaskModel.objects.filter()
            return render(request, 'Api/tasks.html', {'tasks': [t.dict() for t in all_tasks]})
    return redirect('false')

#
def task_delete(request, task_to_delete_id):
    task_to_delete = TaskModel.objects.get(id=task_to_delete_id)
    task_to_delete.delete()
    all_tasks = TaskModel.objects.filter()
    return  render(request, 'Api/tasks.html', {'tasks': [t.dict() for t in all_tasks]})


def task_status(request, task_to_change_status):
    # status_to_change = TaskModel.objects.get(id=task_to_change_status)
    # status_to_change.update(status=2)
    task = TaskModel.objects.filter(id=task_to_change_status).first()
    if task.is_completed == True:
        task.is_completed = False
        task.save()
    else:
        task.is_completed= True
        task.save()
    all_tasks = TaskModel.objects.filter()
    return render(request, 'Api/tasks.html', {'tasks': [t.dict() for t in all_tasks]})

