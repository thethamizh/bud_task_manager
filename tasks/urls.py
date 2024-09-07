from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('tasks', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('reopen/<int:task_id>/', views.reopen_task, name='reopen_task'),
]
