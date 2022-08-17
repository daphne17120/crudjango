from django.db import models

# Create your models here.
class crud2 (models.Model):
    id = models.AutoField(primary_key=True) #Mi id autoincrement
    nombre = models.CharField(max_length=255, verbose_name='nombre')
    apellido = models.CharField(max_length=255, verbose_name='apellido')
    correo = models.CharField(max_length=255, verbose_name='correo')
    telefono = models.CharField(max_length=255, verbose_name='telefono')
    estado = models.CharField(max_length=255, verbose_name='estado') #verbose le ayuda al usuario a saber como se llama el campo
