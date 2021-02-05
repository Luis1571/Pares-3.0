from django.db import models
from Archivos.models import Archivo
from Usuarios.models import Usuario
# Create your models here.
class Documento  (models.Model):
    signatura=models.CharField(primary_key=True, max_length=20)
    titulo=models.CharField(max_length=1000, null=True, blank=True)
    idarchivo=models.ForeignKey (Archivo, null=True, blank=True, on_delete=models.SET_NULL)
    siglo=models.CharField(max_length=15, null=True, blank=True)
    contenido=models.CharField(max_length=10000, null=True, blank=True)
    conservacion=models.CharField(max_length=100, null=True, blank=True) 
    imagen=models.ImageField(upload_to='Documentos', null=True)
   