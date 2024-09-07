from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import *

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')  # Redirect to the task list after sign-up
    else:
        form = SignUpForm()
    return render(request, 'tasks/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('task_list')  # Redirect to the task list after login
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})


@login_required
def task_list(request):
    print(request.POST)
    tasks = Task.objects.all()
    if request.method == 'POST':
        form = TaskStatusForm(request.POST)
        if form.is_valid():
            task_id = request.POST.get('task_id')
            task = Task.objects.get(id = task_id)
            task.status = form.cleaned_data['status']
            task.save()
            return redirect('task_list')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
             


    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        due_date = request.POST.get('due_date', None)
        Task.objects.create(title=title, description=description, due_date=due_date, user=request.user)
        return redirect('task_list')
    return render(request, 'tasks/create_task.html')

@login_required
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.completed = True
    task.save()
    return redirect('task_list')

@login_required
def reopen_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.completed = False
    task.save()
    return redirect('task_list')
