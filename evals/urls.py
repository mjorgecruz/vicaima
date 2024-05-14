from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path('addlogin/', views.addLogin, name="addlogin"),
	path('login/', views.login_view, name="login"),

]
