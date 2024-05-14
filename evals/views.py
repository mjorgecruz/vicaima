from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from .forms import NewLogin
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def index(request):
	return render(request, "evals/index.html")

def addLogin(request):
    if request.method == 'POST':
        form = NewLogin(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NewLogin()

    return render(request, 'main/login.html',  {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']  # use 'username' instead of 'user'
        password = request.POST['password']
        try:
            user = Login.objects.get(username=username)
            if user.check_password(password):
                return user
            else:
                return None
        except ObjectDoesNotExist:
            return None
