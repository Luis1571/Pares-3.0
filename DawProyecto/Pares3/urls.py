from django.urls import path
from .views import index, home,archivos,noticias,busqueda, contacto, usuarios,Acceso_con_Registro, buscarDoc, detalleDocumento,verMisDocumentos, login,formRegistro,registrarUsuario, guardarDoc, Eliminar_historial_Doc

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="index"),
    path('noticias/',noticias ,name="noticias" ),
    path('archivos/', archivos,name="archivos" ),
    path('busqueda/', busqueda,name="busqueda" ),
    path('contacto/', contacto, name="contacto" ),
    path('usuarios/', usuarios, name="usuarios" ),
    path('verMisDocumentos/<nombre>', verMisDocumentos, name="verMisDocumentos" ),
    path('home/', home, name="home"),
    path('buscarDoc/', buscarDoc, name="ResultadoBusqueda"),
    path('Acceso_con_Registro/', Acceso_con_Registro, name="Acceso_con_Registro" ),
    path('login/', login, name="login" ),
    path('detalleDocumento/<signatura>', detalleDocumento, name="detalleDocumento" ),
    path('formRegistro/', formRegistro, name="formRegistro" ),
    path('registrarUsuario/', registrarUsuario, name="registrarUsuario" ),
    path('guardarDoc/<signatura>', guardarDoc, name="guardarDoc" ),
    path('Eliminar_historial_Doc/<signatura>', Eliminar_historial_Doc, name="Eliminar_historial_Doc" ),
    
    


]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)