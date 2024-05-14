from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Colaboradores, Login

class NewUserForm(UserCreationForm):
    username = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username','password']

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user
