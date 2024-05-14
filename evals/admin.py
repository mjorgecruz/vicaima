from django.contrib import admin
from django.urls import path, include
from .models import *

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('evals.urls')),
]

# Register your models here.
admin.site.register(Login)
admin.site.register(Colaboradores)
