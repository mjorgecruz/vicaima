from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from .forms import NewLogin

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