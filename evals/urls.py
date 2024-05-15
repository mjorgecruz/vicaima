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
	path('dashboard_users_list', views.dashboard_users_list, name='dashboard_users_list'),
	path('import', views.import_view, name="import"),

	path('dashboard_add_new_eval', views.dashboard_add_event, name='dashboard_add_new_eval'),
	path('dashboard_add_edit_eval', views.eval_view, name='dashboard_add_new_eval'),
	path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
	path('delete_collaborator/<int:collaborator_id>/', views.delete_collaborator, name='delete_collaborator'),

	path('', include('django.contrib.auth.urls'))
]

