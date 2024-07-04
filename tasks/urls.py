from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    task_detail,
    task_create,
    task_update,
    task_delete,
    api_task_list,
    dashboard,
    calendar,
    members,
    task_create,
)

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/', task_detail, name='task_detail'),
    path('task/new/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('api/tasks/', api_task_list, name='api_task_list'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard', dashboard, name='dashboard'),
    path('calendar/', calendar, name='calendar'),
    path('members/', members, name='members'),
    path('create/', task_create, name='task_create'),

]
