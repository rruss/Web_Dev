from django.urls import path, re_path
from . import views

urlpatterns = [
    path('task_lists/', views.Lists.as_view()),
    path('task_lists/<int:pk>/', views.TaskListDetail.as_view()),
    path('task_lists/<int:pk>/tasks/', views.TasksFromList.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
    path('users/', views.UserList.as_view()),
]
