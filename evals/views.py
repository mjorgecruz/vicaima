from .forms import UploadFileForm
from django.shortcuts import render, redirect
from django.contrib import messages
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
from django.db import connection, transaction

from .forms import CreateUserForm, LoginForm, NewUserForm
from .forms import CreateUserForm, LoginForm, NewUserForm, NewEventForm, NewAvaliadosForm
from .models import Colaboradores, Eventos, Avaliados, Resultados

from tablib import Dataset
from datetime import datetime
import csv
import pandas as pd
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


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

import sqlite3
import pandas as pd

import chardet
from io import StringIO

def import_view(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']            
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'Please upload a valid CSV file.')
                return render(request, 'something')
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM sqlite_sequence WHERE name = '" + Colaboradores._meta.db_table + "'")
                cursor.execute("DELETE FROM sqlite_sequence WHERE name = '" + User._meta.db_table + "'")  # Reset User ID sequence
                transaction.commit()
                file_data = csv_file.read().decode('utf-8')  # Read the file data and decode it as UTF-8
                reader = csv.DictReader(StringIO(file_data))
                for row in reader:
                    nickname = row['Nome'] + " " + row['Apelido']
                    Colaboradores.objects.create(
                        nickname=nickname,
                        name=row['Nome'],
                        last_name=row['Apelido'],
                        department=row['Departamento'],
                        function=row['Funcao'],
                        admission_date=datetime.strptime(row['Data de Admissao'], '%d/%m/%Y').date(),
                        functional_group=row['Grupo Funcional:'],
                        password=" "
                    )
                    User.objects.create_user(  # Create a User instance
                        username=nickname,
                        password="admin12345",
                        first_name=row['Nome'],
                        last_name=row['Apelido'],
            )
                
    form = UploadFileForm()
    return render(request, "evals/import.html", {'form': form})

def dashboard_admin(request):
    eventos = Eventos.objects.all()
    return render(request, "evals/dashboard_admin.html", {'eventos': eventos})

def dashboard_user(request):
    return render(request, "evals/dashboard_user.html")

def dashboard_user_edit(request):
    return render(request, "evals/dashboard_user_edit.html")

def dashboard_user_evaluate(request):
    return render(request, "evals/dashboard_user_evaluate.html")

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
        event_form = NewEventForm(request.POST)
        if event_form.is_valid():
            event = event_form.save()  # Save the event form and get the instance
            eval_form = NewAvaliadosForm(request.POST)  # Initialize the form with POST data
            if eval_form.is_valid():
                eval = eval_form.save(commit=False)  # Don't save the form to the database yet
                eval.evaluation_id = event  # Assign the event id to the eval form
                eval.save()  # Now save the form to the database
                evaluated_ids = request.POST.getlist('evaluated_id')  # Get list of evaluated_ids
                for evaluated_id in evaluated_ids:
                    eval.evaluated_id.add(evaluated_id) 
                return redirect('dashboard_admin')
    else:
        event_form = NewEventForm()
        eval_form = NewAvaliadosForm()
    return render(request, 'evals/dashboard_add_new_eval.html', {'event_form': event_form, 'eval_form': eval_form})

from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

@require_POST
def delete_event(request, event_id):
    event = get_object_or_404(Eventos, id=event_id)  # Get the event or return 404 if not found
    event.delete()  # Delete the event
    return redirect('dashboard_admin')  # Redirect to the admin dashboard

@require_POST
def delete_collaborator(request, collaborator_id):
    collaborator = get_object_or_404(Colaboradores, id=collaborator_id)  # Get the collaborator or return 404 if not found
    user = get_object_or_404(User, username=collaborator.nickname)  # Get the User instance with the same username
    collaborator.delete()  # Delete the collaborator
    user.delete()  # Delete the User instance
    return redirect('dashboard_users_list')

def eval_view(request):
    return render(request, "evals/eval_form.html")