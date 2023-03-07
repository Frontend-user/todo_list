from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.tasks, name='tasks'),
    path('lists/', views.lists, name='lists'),
    path('lists/create/', views.list_create, name='list_create'),
    path('lists/<int:list_to_delete_id>/delete/', views.list_delete, name='list_delete'),
    path('lists/<int:list_id>/open/', views.list_open, name="list_open"),
    path('tasks/false/', views.false, name='false'),
    path('tasks/create/<int:list_id>/', views.task_create, name='task_create'),
    path('tasks/<int:task_to_change_status>/status/<int:list_id>/', views.task_status, name='task_status'),
    path('tasks/<int:task_to_delete_id>/delete/', views.task_delete, name='task_delete'),
    path('base/', views.base, name='base'),
    path('tasks/<int:task_to_move_id>/move/', views.lists_to_move, name='task_move'),
    path('lists/<int:list_where_move_id>/list_move/<int:task_to_move_id>/', views.task_move_to_list, name='list_move'),
]
