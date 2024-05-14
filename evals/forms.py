from django.forms import ModelForm
from django import forms
from .models import Colaboradores
from .models import Login

class NewLogin(ModelForm):
    class Meta:
        model = Login
        fields = '__all__'
    
class NewLogin(ModelForm):
    class Meta:
        model = Login
        fields = ['username','password','permission', 'employee_id']

class UploadFileForm(forms.Form):
    file = forms.FileField()
