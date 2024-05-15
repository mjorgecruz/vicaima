from django.shortcuts import render, redirect
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
