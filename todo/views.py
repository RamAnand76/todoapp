from datetime import date, datetime
from django.shortcuts import render, redirect
from .forms import TodoItemForm
from .models import Task, CompletedTask
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User



def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                error_message = "Username is already taken."
                return render(request, 'signup.html', {'form': form, 'error_message': error_message})
            
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_list')
    return render(request, 'login.html')

@login_required
def task_list(request):
    print(request.user)
    user = request.user
    tasks = Task.objects.filter(user=user)
    completed_tasks = CompletedTask.objects.filter(user=user)
    show_completed = False

    if request.method == 'POST':
        if 'completed' in request.POST:
            show_completed = True

    expired_tasks = Task.objects.filter(completed=False, completed_at__lt=date.today())
    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
        'show_completed': show_completed,
        'expired_tasks': expired_tasks,
    }
    return render(request, 'tasks/task_list.html', context)


@login_required
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        completed_at = request.POST.get('completed_at')  # Get the expiry date from the form

        user = request.user  # Get the current user

        task = Task.objects.create(
            title=title,
            description=description,
            priority=priority,
            completed_at=completed_at,  # Convert the expiry_date string to datetime object
            user=user
        )
        return redirect('task_list')

    return render(request, 'tasks/task_create.html')


@login_required
def task_edit(request, task_id):
    user = request.user
    try:
        task = Task.objects.get(id=task_id, user=user)
        if request.method == 'POST':
            form = TodoItemForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('task_list')
        else:
            form = TodoItemForm(instance=task)
        context = {
            'form': form,
            'task_id': task_id,
        }
        return render(request, 'tasks/task_edit.html', context)
    except Task.DoesNotExist:
        # Handle the case when the task does not exist or does not belong to the user
        return redirect('task_list', task_id=task_id)






@login_required
def task_delete(request, task_id):
    user = request.user
    try:
        task = Task.objects.get(id=task_id, user=user)
        completed_task = CompletedTask.objects.create(
            user=user,
            title=task.title,
            description=task.description
        )
        task.delete()
    except Task.DoesNotExist:
        # Handle the case when the task does not exist or does not belong to the user
        return redirect('task_list')

    return redirect('task_list')



@login_required
def task_remove(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')


@login_required
def task_complete(request, task_id):
    user = request.user
    try:
        task = Task.objects.get(id=task_id, user=user)
        task.completed = True
        task.save()
    except Task.DoesNotExist:
        # Handle the case when the task does not exist or does not belong to the user
        return redirect('task_list')
    return redirect('task_list')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login_view')


from django.views.generic.edit import UpdateView





def redirect_to_task_list(request):
    return redirect('task_list')