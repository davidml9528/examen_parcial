from django.db import models

# Create your models here.
class usuariosRegistrados(models.Model):
    nombre = models.CharField(max_length=128,default='')
    apellido = models.CharField(max_length=128,default='')
    password = models.CharField(max_length=128,default='')
    codigoUsuario = models.CharField(max_length=128,default='')
class tarea(models.Model):
    descripcion = models.CharField(max_length=128,default='')
    fechaCreacion = models.CharField(max_length=128,default='')
    usuarioResponsable = models.CharField(max_length=128,default='')
    estadoTarea = models.CharField(max_length=128,default='')

