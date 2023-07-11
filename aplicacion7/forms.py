from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group, Permission #con esto se trae user segun lo creado class meta que tiene user
from .models import Tarea, Paciente

class UserRegistrationForm(UserCreationForm):# hereda de usercreationform y se trae este formato arriba from django....
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmacion contraseña", widget=forms.PasswordInput)
    date = forms.DateField()
    group = forms.ModelChoiceField(queryset=Group.objects.all())
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta: #sirve para agregar info que se usara solamente en este tipo de objeto
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UsuarioForm(forms.Form):#clase que trae todas la validaciones Form y que deben ponerse todos los campos como formulario nuevo a diferencia de class escuela abajo
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)

class PacienteForm(forms.ModelForm):#model form. trae su propio modelo, ver models.py
    class Meta:
        model = Paciente
        fields = '__all__' 


class TareaForm(forms.ModelForm):#model form. trae su propio modelo, ver models.py
    class Meta:
        model = Tarea
        fields = '__all__' 