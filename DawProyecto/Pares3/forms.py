from django import forms
from Usuarios.models import Usuario

class Nuevo_user_form(forms.ModelForm):
    class Meta:
        model=Usuario
        fields = '__all__'