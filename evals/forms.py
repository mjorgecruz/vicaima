from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Colaboradores, Login, Eventos, Avaliados, Resultados

# create a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2', 'is_staff']

#authenticate user

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        username = forms.CharField(widget=TextInput())
        password = forms.CharField(widget=PasswordInput())

#add new user
class NewUserForm(forms.ModelForm):
    model = Colaboradores
    nickname = forms.CharField(widget=TextInput())
    name = forms.CharField(widget=TextInput())
    last_name = forms.CharField(widget=TextInput())
    department = forms.CharField(widget=TextInput())
    function = forms.CharField(widget=TextInput())
    admission_date = forms.DateField(widget=forms.SelectDateWidget)
    functional_group = forms.CharField(widget=TextInput())
    class Meta:
        model = Colaboradores
        fields = ['name', 'last_name', 'department', 'function', 'admission_date', 'functional_group']

class NewEventForm(forms.ModelForm):
    creation_date = forms.DateField(widget=forms.SelectDateWidget)
    deadline = forms.DateField(widget=forms.SelectDateWidget)
    evaluator_id = forms.ModelChoiceField(queryset=Colaboradores.objects.all(), empty_label="Select a user")
    class Meta:
        model= Eventos
        fields = ['creation_date', 'deadline', 'evaluator_id']
    def __init__(self, *args, **kwargs):
        super(NewEventForm, self).__init__(*args, **kwargs)
        self.fields['evaluator_id'].label_from_instance = lambda obj: f"{obj.nickname}"

class NewAvaliadosForm(forms.ModelForm):
    evaluation_id = forms.ModelChoiceField(queryset=Eventos.objects.all(), empty_label="Select an event")
    evaluated_id = forms.ModelMultipleChoiceField(queryset=Colaboradores.objects.all())
    # results_id = forms.ModelChoiceField(queryset=Resultados.objects.all(), empty_label="Select a result")
    class Meta:
        model = Avaliados
        fields = ['evaluation_id', 'evaluated_id']

class NewResultadosForm(forms.ModelForm):
    result_id = forms.ModelChoiceField(queryset=Avaliados.objects.all(), empty_label="Select an evaluation")
    class Meta:
        model = Resultados
        fields = ['result_id']