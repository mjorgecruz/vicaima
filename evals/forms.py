from django.forms import ModelForm
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
