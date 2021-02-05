from django.db import models
# Create your models here.
class Usuario (models.Model):
    idUsusario=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50, null=True, blank=True)
    apellido1=models.CharField(max_length=50 , null=True, blank=True) 
    apellido2=models.CharField(max_length=50 )
    email=models.EmailField(max_length=70 , null=True, blank=True, unique =True)
    telefono=models.BigIntegerField(null=True, blank=True)
    pais=models.CharField(max_length=30, null=True, blank=True)
    password=models.CharField(max_length=500 , null=True, blank=True)