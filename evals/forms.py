from django.forms import ModelForm
from .models import Employee

class NewEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        
class NewEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name','email','phone','course']