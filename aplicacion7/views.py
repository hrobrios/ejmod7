from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegistrationForm
from .forms import UsuarioForm, TareaForm
from .models import Usuario, Tarea
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# Create your views here.


def inicio(request):
    return render(request, "home.html")

@login_required
def register_user(request):#el request es todo lo que traemos desde hmtl
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)#se crea instancia userregistration
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data['group']
            permissions = form.cleaned_data['permissions']
            username = form.cleaned_data['username']
            user.groups.add(group)
            user.user_permissions.set(permissions)
            messages.success(request, f'Usuario {username} creado exitosamente!!')
            return redirect('home')
    else: #si no hago post, devolverá al formulario register user
        form = UserRegistrationForm()
    
    context = {'form': form}
    return render(request, 'register_user.html', context)


@login_required
def home(request):
    users = User.objects.all() #ESTO  ES TRAER BASE DE DATOS PARA EXTRAER INFO
#OBJECTS CON S ES UNA FUNCION PARA TRAER ALGO DE UNA TABLA, INTERACTUA ON LA BASE DE DATOS
# USER (BASE DA DATOS), OBJECTS(MANEJA LA INFO), ALL (METODO QUE TRAE TODOS LAS FILAS DE LA TABLA USER)   
    nuevos = ["", ""]

    context = {
        "usuarios": users,
        "otros": nuevos,
    }

    return render(request, "users.html", context=context)


@login_required
def crear_usuario(request):
    form = UsuarioForm()

    if request.method == "POST":#post trae info solicitada con get
        print(request)
        form = UsuarioForm(request.POST)#trae un formulario que se base en el post

        if form.is_valid():#se validará lo que coincida en el modelo creado en el FORMS:PY
            print(form)
            usuario = Usuario()#se crea el objeto del modelo y el cleaned_data filtra el imput que traemos
            usuario.nombre = form.cleaned_data['nombre']
            usuario.apellido = form.cleaned_data['apellido']
            usuario.save()
        else:
            print("Datos invalidos")
        return redirect('/home')
    
    context = {
        'form': form
    }

    return render(request, 'formulariouser.html', context=context)


@login_required
def tareas(request):
    form = TareaForm()

    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            print(form)
            tarea = Tarea()
            tarea.nombre = form.cleaned_data['nombre']
            tarea.tema = form.cleaned_data['tema']
            tarea.fecha = form.cleaned_data['fecha']
            tarea.save()
        else:
            print("Datos invalidos")
        return redirect('/mostrartarea')
    context = {'form': form}

    return render(request, 'tareas.html', context=context)#se pone aplicacion+el nombre del html, porque tempmlate/tiene dentro aplicacion. en su defecto de hace directo

@login_required
def mostrartarea(request):

    datos = Tarea.objects.all()

    context = {'tareas': datos}

    return render(request, 'mostrartarea.html', context=context)