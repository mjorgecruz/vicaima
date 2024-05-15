from django.shortcuts import render, redirect
from .forms import UploadFileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.contrib import messages
from .forms import UploadFileForm
from .models import Login, Colaboradores
from tablib import Dataset
import csv
import pandas as pd
from datetime import datetime

from .forms import CreateUserForm, LoginForm, NewUserForm
from .forms import CreateUserForm, LoginForm, NewUserForm, NewEventForm, NewAvaliadosForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from .models import Colaboradores, Eventos, Avaliados, Resultados


def homepage(request):
    return render(request, "evals/index.html")

def register(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')
    context = {'registerform': form}
    return render(request, "evals/register.html", context=context)

def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid:
            username = request.POST.get('username')
            password = request.POST.get('password')
            is_staff = request.POST.get('is_staff')
            user = authenticate(request, username=username, password=password, is_staff=is_staff)
            if user is not None:
                auth.login(request, user)
                if user.is_staff == True:
                    return redirect('dashboard_admin')
                else:
                    return redirect('dashboard_user')
    context = {'loginform':form}
    return render(request, "evals/my-login.html", context=context)

def import_view(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']

            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'Please upload a valid CSV file.')
                return render(request, 'something')
            
            try:
                decoded_data = csv_file.read().decode('utf-8')
                print(decoded_data)

                dataset = Dataset()
                dataset.csv = decoded_data
                imported_data = dataset.dict
                
                for data in imported_data:
                    try:
                        # Parsing admission date with a fallback for empty or invalid date strings
                        admission_date_str = data.get('Data de admissao', '')
                        admission_date = datetime.now().date()
                        if admission_date_str:
                            admission_date = datetime.strptime(admission_date_str, '%d/%m/%Y').date()
                    except ValueError:
                        messages.error(request, f'Invalid date format: {admission_date_str}')
                        continue  # Skip this row if the date format is invalid
                    Colaboradores.objects.create(
                        colaborador_id = data.get('N colaborador', ''),
                        name = data.get('Nome', ''),
                        last_name = data.get('Apelido', '6'),
                        department = data.get('Departamento', '1'),
                        function = data.get('Funcao', '2'),
                        admission_date = admission_date,
                        functional_group = data.get('Grupo Funcional', '')
                    )
                print()
                messages.success(request, 'User created with success')
            except UnicodeDecodeError:
                    messages.error(request, 'Failed to decode the file. Please ensure it is encoded in UTF-8 or ISO-8859-1.')
                    return render(request, "pages/import/import.html", {'form': form})

            return render(request, 'evals/index.html')

    else:
        form = UploadFileForm()
    return render(request, "pages/import/import.html", {'form': form})

def dashboard_admin(request):
    eventos = Eventos.objects.all()
    return render(request, "evals/dashboard_admin.html", {'eventos': eventos})

def dashboard_user(request):
    return render(request, "evals/dashboard_user.html")

def dashboard_add_collaborator(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('dashboard_admin')
    else:
        form = NewUserForm()
    context = {'newuserform': form}
    return render(request, "evals/dashboard_add_collaborator.html", context=context)

def dashboard_users_list(request):
    collaborators = Colaboradores.objects.all()
    return render(request, "evals/dashboard_users_list.html", {'collaborators': collaborators})

def dashboard_add_event(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = (request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_admin')
    else:
        form = NewUserForm()
    context = {'newuserform': form}
    return render(request, "evals/dashboard_add_collaborator.html", context=context)

def dashboard_add_event(request):
    if request.method == 'POST':
        eval_form = NewAvaliadosForm
        event_form = NewEventForm(request.POST)
        if event_form.is_valid():
            event = event_form.save()  # Save the event form and get the instance
            eval_form = (request.POST)
            if eval_form.is_valid():
                eval = eval_form.save(commit=False)  # Don't save the form to the database yet
                eval.event = event  # Assign the event id to the eval form
                eval.save()  # Now save the form to the database
                return redirect('dashboard_admin')
    else:
        event_form = NewEventForm()
        eval_form = NewAvaliadosForm()

    return render(request, "evals/dashboard_add_new_eval.html", {'neweventform': event_form, 'newavaliadosform': eval_form})
