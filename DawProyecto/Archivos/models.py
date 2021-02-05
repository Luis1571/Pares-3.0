from django.db import models

# Create your models here.
class Archivo (models.Model):
    idArchivo=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100, null=True, blank=True) 
    descripcion=models.CharField(max_length=1000,null=True, blank=True )
    email=models.EmailField(max_length=70, null=True, blank=True)
    imagen=models.ImageField(upload_to='Archivos')
