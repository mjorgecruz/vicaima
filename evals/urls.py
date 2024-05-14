from django.contrib  import admin
from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.homepage, name=''),
	path('register', views.register, name='register'),
	path('my-login', views.my_login, name='my-login'),
	path('dashboard_admin', views.dashboard_admin, name='dashboard_admin'),
	path('dashboard_user', views.dashboard_user, name='dashboard_user'),
	path('dashboard_add_collaborator', views.dashboard_add_collaborator, name='dashboard_add_collaborator'),

	path('', include('django.contrib.auth.urls'))
]

