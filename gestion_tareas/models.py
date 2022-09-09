from django.db import models
from datetime import date,datetime
# Create your models here.
class usuariosRegistrados(models.Model):
    nombre = models.CharField(max_length=128,default='')
    apellido = models.CharField(max_length=128,default='')
    password = models.CharField(max_length=128,default='')
    codigoUsuario = models.CharField(max_length=128,default='')
class tarea(models.Model):
    descripcion = models.CharField(max_length=128,default='')
    fechaCreacion = models.DateField(default=datetime.today())
    fechaEntrega = models.DateField(default=datetime.today())
    usuarioResponsable = models.CharField(max_length=128,default='')
    estadoTarea = models.CharField(max_length=128,default='PROGRESO')
