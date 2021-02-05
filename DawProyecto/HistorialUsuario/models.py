from django.db import models
from Usuarios.models import Usuario
from Documentos.models import Documento

class HistoriaUser (models.Model):
    idhistorial=models.AutoField(primary_key=True)
    idusuario=models.ForeignKey (Usuario, null=True, blank=True, on_delete=models.SET_NULL)
    signatura=models.ForeignKey (Documento, null=True, blank=True, on_delete=models.SET_NULL)
    fecha=models.DateField(auto_now_add=True)
    