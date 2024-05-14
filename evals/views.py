from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from .forms import NewLogin, UploadFileForm
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
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = Login.objects.get(username=username)
        except Login.DoesNotExist:
            return render(request, 'pages/login/login.html')
        if password == user.password:
            return redirect('/index')
        else:
            return render(request, 'pages/login/login.html')
    else:
        return render(request, 'pages/login/login.html')

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