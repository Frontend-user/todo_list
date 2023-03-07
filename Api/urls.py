from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/false/', views.false, name='false'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:task_to_change_status>/status/', views.task_status, name='task_status'),
    path('tasks/<int:task_to_delete_id>/delete/', views.task_delete, name='task_delete'),

]