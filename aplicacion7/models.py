from django.db import models

# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    

    def __str__(self):
        return self.apellido
    


class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    tema = models.CharField(max_length=100)
    fecha = models.CharField()

    def __str__(self):
        return self.nombre