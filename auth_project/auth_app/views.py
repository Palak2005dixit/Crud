from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib import messages
from .models import Task
from .forms import RegisterForm


# ================= LOGIN =================

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True


# ================= LOGOUT =================

def custom_logout(request):
    logout(request)
    return redirect('login')


# ================= HOME =================

def home(request):
    return redirect('login')


# ================= REGISTER =================

def register_view(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Successfully Registered! Please Login.")
        return redirect('login')

    return render(request, 'register.html', {'form': form})


# ================= DASHBOARD =================

@login_required(login_url='login')
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'tasks': tasks})


# ================= CREATE TASK =================

@login_required(login_url='login')
def create_task(request):
    if request.method == 'POST':
        Task.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            description=request.POST.get('description')
        )
        messages.success(request, "Task Added Successfully!")
    return redirect('dashboard')


# ================= EDIT TASK =================

@login_required(login_url='login')
def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        messages.success(request, "Task Updated Successfully!")
        return redirect('dashboard')

    tasks = Task.objects.filter(user=request.user)

    return render(request, 'dashboard.html', {
        'tasks': tasks,
        'edit_task': task
    })


# ================= DELETE TASK =================

@login_required(login_url='login')
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    task.delete()
    messages.success(request, "Task Deleted Successfully!")
    return redirect('dashboard')
