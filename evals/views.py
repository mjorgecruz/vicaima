from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    return render(request, 'main/home.html')

def addLogin(request):
    if request.method == 'POST':
        form = (request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redirect to login page after successful registration
    else:
        form = NewUserForm()
    return render(request, 'main/login.html',  {'form': form})

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('evals/index')  # replace 'home' with your desired redirect
        else:
            return render(request, 'pages/login/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'pages/login/login.html')
