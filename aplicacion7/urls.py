from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('', views.inicio, name='home'),
    path('acceso/', views.acceso, name="acceso"),
    path('users/', views.home, name="users"),
    path('register_user/', views.register_user, name='register_user'),
    #path('formulariouser/', views.crear_usuario, name='formulariouser'),
    path("pacientes/", views.pacientes, name="pacientes"),
    path('mostrarpaciente/', views.mostrarpaciente, name='mostrarpaciente'),
    path("ficha1/", views.ficha1, name="ficha1"),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='aplicacion/login.html'), name='login'),

    path('tareas/', views.tareas, name='tareas'),
    path('mostrartarea/', views.mostrartarea, name='mostrartarea'),
    
]