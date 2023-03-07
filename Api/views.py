from django.shortcuts import render, redirect
from .forms import TaskForm, ListForm
from .models import TaskModel, ListModel
from django.http import HttpResponse


def index(request):
    return render(request, 'Api/index.html')


def tasks(request):
    all_tasks = TaskModel.objects.filter()
    return render(request, 'Api/tasks.html', {'tasks': [t.dict() for t in all_tasks]})


def false(request):
    return render(request, 'Api/false.html')


def task_create(request, list_id):
    if request.method == 'POST':
        task = TaskForm(request.POST)
        if task.is_valid():
            text = task.cleaned_data['text']
            TaskModel.objects.create(text=text, list_id=list_id)
            return redirect(f'/lists/{list_id}/open/')
    return redirect('false')


#
def task_delete(request, task_to_delete_id):
    task_to_delete = TaskModel.objects.get(id=task_to_delete_id)
    list_id = task_to_delete.list_id
    task_to_delete.delete()
    return redirect(f'/lists/{list_id}/open/')

def task_status(request, task_to_change_status, list_id):
    task = TaskModel.objects.filter(id=task_to_change_status).first()
    if task.is_completed == True:
        task.is_completed = False
        task.save()
    else:
        task.is_completed = True
        task.save()
    return redirect(f'/lists/{list_id}/open/')


def lists(request):
    all_lists = ListModel.objects.filter()
    return render(request, 'Api/lists.html', {'lists': [l.dict() for l in all_lists]})


def list_create(request):
    if request.method == 'POST':
        list = ListForm(request.POST)
        if list.is_valid():
            name = list.cleaned_data['name']
            ListModel.objects.create(name=name)
            all_lists = ListModel.objects.filter()
            return redirect('/lists/')
    return redirect('false')


def list_delete(request, list_to_delete_id):
    list_to_delete = ListModel.objects.get(id=list_to_delete_id)
    list_to_delete.delete()
    return redirect('/lists/')


def list_open(request, list_id):
    list_to_open = ListModel.objects.get(id=list_id)
    list_tasks = TaskModel.objects.filter(list_id=list_to_open.id)
    return render(request, 'Api/list_open.html', {'list_to_open': list_to_open.dict(), 'tasks': list_tasks})
