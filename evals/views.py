from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from .models import Employee

def index(request):
	return render(request, "evals/index.html")
# Create your views here.

# def addEmployee(request):
#     form = NewEmployeeForm
#     context = {'form':form}
#     return render(request, 'accounts/add-employee.html', context)