from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.forms import ModelForm
from django import forms
from .models import Colaboradores
from .models import Login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Colaboradores, Login

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
    name = forms.CharField(widget=TextInput())
    last_name = forms.CharField(widget=TextInput())
    department = forms.CharField(widget=TextInput())
    function = forms.CharField(widget=TextInput())
    admission_date = forms.DateField(widget=forms.SelectDateWidget)
    functional_group = forms.CharField(widget=TextInput())
    class Meta:
        model = Colaboradores
        fields = ['name', 'last_name', 'department', 'function', 'admission_date', 'functional_group']

class NewUserForm(forms.ModelForm):
    model = Colaboradores
    name = forms.CharField(widget=TextInput())
    last_name = forms.CharField(widget=TextInput())
    department = forms.CharField(widget=TextInput())
    function = forms.CharField(widget=TextInput())
    admission_date = forms.DateField(widget=forms.SelectDateWidget)
    functional_group = forms.CharField(widget=TextInput())
    class Meta:
        model = Colaboradores
        fields = ['name', 'last_name', 'department', 'function', 'admission_date', 'functional_group']
