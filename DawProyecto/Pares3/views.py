#importaciones de librerías y clases del proyecto
from django.shortcuts import render, HttpResponse,redirect
from Archivos.models import Archivo
from Usuarios.models import Usuario
from Documentos.models import Documento
from HistorialUsuario.models import HistoriaUser
from django.contrib import  messages
import hashlib
from .forms import Nuevo_user_form

# Función inicial redirecciona a la plantilla principal
def index (request):
    return render (request, "Pares3/index.html")

# Función que toma los valores del formulario inicial 
def Acceso_con_Registro(request):
    if request.POST["email"] and request.POST["pw"]: 
        emailIntroducido=request.POST["email"]
        passIntroducido = request.POST["pw"]
        pwEncriptado=encriptar(passIntroducido)
        Usuario_Introducido = Usuario.objects.filter(email__icontains=emailIntroducido)
        if len(Usuario_Introducido)!=0:
            for i in Usuario_Introducido:
            # Guardamos los  valores de la sesion 
                nombre=request.session['nombre']=i.nombre
                email=request.session['email']=i.email
                a1=request.session['apellido1']=i.apellido1
                a2=request.session['apellido2']=i.apellido2
                telefono=request.session['telefono']=i.telefono
                pais=request.session['pais']=i.pais
                
                print(nombre) 
                if i.email==emailIntroducido and i.password==pwEncriptado:
               
                    return render(request, "Pares3/home.html", {"nombre": nombre} )
                else:    
                    error2="El email y la contraseña no coinciden"
                    return render (request, "Pares3/index.html", {"mensaje_login": error2})
        else:    
            error="Datos erróneos, por favor, escriba correctamente los datos"
            return render (request, "Pares3/index.html", {"mensaje_login": error})
    else :
        mensaje="Por favor, escriba en ambos campos"
        return render (request, "Pares3/index.html", {"mensaje_login": mensaje})


# Funcion tras el login inicial con dos opciones: si registró o no 
def home(request):
    # si se ha registrado en el sesion se guarda el nombre 
    if request.session.get('nombre'):
        nombre=request.session.get('nombre')
        return render(request, "Pares3/home.html" , {'nombre':nombre}  )
    else:
       return render(request, "Pares3/home.html"  ) 


def noticias(request):
    if request.session.get('nombre'):
        nombre=request.session.get('nombre')
        return render(request, "Pares3/noticias.html" , {'nombre':nombre}  )
    else:
           return render(request, "Pares3/noticias.html"  )
    
#Funcion que busca en la tabla Archivos todo su contenido 
def archivos(request):
    if request.session.get('nombre'):
        nombre=request.session.get('nombre')
        archivos = Archivo.objects.all()
        return render(request, "Pares3/archivos.html", {"archivos":archivos, 'nombre':nombre} )
    else:
        archivos = Archivo.objects.all()
        return render(request, "Pares3/archivos.html", {"archivos":archivos} )

#Redirección al html busqueda 
def busqueda(request):
    if request.session.get('nombre'):
        nombre=request.session.get('nombre')
        return render(request, "Pares3/busqueda.html" , {'nombre':nombre}  )
    else:
           return render(request, "Pares3/busqueda.html"  )

def formRegistro(request):
    form=Nuevo_user_form()
    
    return render(request, "Pares3/registro.html", {'formularioNewUser':form}  )  
    

def contacto(request):
    if request.session.get('nombre'):
        nombre=request.session.get('nombre')
        return render(request, "Pares3/contacto.html" , {'nombre':nombre}  )
    else:
           return render(request, "Pares3/contacto.html"  )
       
    
def usuarios (request):
    if request.session.get('nombre'):
        nombre=request.session.get('nombre')
        email=request.session.get('email')
        a1=request.session.get('apellido1')
        a2=request.session.get('apellido2')
        tel=request.session.get('telefono')
        pais=request.session.get('pais')
        return render(request, "Pares3/perfil.html" , {'nombre':nombre, 'email':email, 'pais':pais, 'tel':tel,
        'a1':a1, 'a2':a2}  )
    else:
           return render(request, "Pares3/login.html"  )
    

def login(request):
    if request.POST["email"] and request.POST["pw"]:
        emailIntroducido=request.POST["email"]
        passIntroducido = request.POST["pw"]
        pwEncriptado=encriptar(passIntroducido)
        print(pwEncriptado)
        print(emailIntroducido)
        print(passIntroducido)
        Usuario_Introducido = Usuario.objects.filter(email__icontains=emailIntroducido)
        if len(Usuario_Introducido)!=0:
            print(type(Usuario_Introducido)) 
            print(len(Usuario_Introducido))
            for i in Usuario_Introducido:

                if i.email==emailIntroducido and i.password==pwEncriptado:
                    nombre=request.session['nombre']=i.nombre
                    email=request.session['email']=i.email
                    a1=request.session['apellido1']=i.apellido1
                    a2=request.session['apellido2']=i.apellido2
                    tel=request.session['telefono']=i.telefono
                    pais=request.session['pais']=i.pais
               
                    return render(request, "Pares3/perfil.html",{'nombre':nombre, 'email':email, 'pais':pais, 'tel': tel, 'a1':a1, 'a2':a2} )
                else:    
                    error2="El email y la contraseña no coinciden"
                    return render (request, "Pares3/login.html", {"mensaje_login2": error2})
        else :
            error="No se ha encontrado ningun usuario con ese email "
            return render (request, "Pares3/login.html", {"mensaje_login2": error})
    else :
        mensaje="Por favor, escriba en ambos campos"
        return render (request, "Pares3/login.html", {"mensaje_login2": mensaje})




       

########## método para encriptar el 
def encriptar(passIntroducido):
    print("entra")
    sha_signature = \
        hashlib.sha256(passIntroducido.encode()).hexdigest()
    return sha_signature




def buscarDoc(request):
    # Busqueda por signatura 
   if request.GET["Signatura"]:
       signaturaSolicitado = request.GET["Signatura"]
       documentos = Documento.objects.filter(
            signatura__icontains=signaturaSolicitado)
       if len(documentos)!=0:
            return render(request, "Pares3/busqueda.html", {"documentos": documentos} )
       else:
           error="No se ha encontrado ninguna signatura similar"
           return render(request, "Pares3/busqueda.html", {"mensaje_busqueda": error} )

    #  Busqueda por archivos       
   if request.GET["Archivo"]:
       archivoSolicitado = request.GET["Archivo"]
       documentos = Documento.objects.filter(
           idarchivo__nombre__icontains=archivoSolicitado)
       if len(documentos)!=0:
            return render(request, "Pares3/busqueda.html", {"documentos": documentos} )
       else:
           error="No se ha encontrado ningún archivo con ese nombre"
           return render(request, "Pares3/busqueda.html", {"mensaje_busqueda": error} )
       
    # Busqueda por el  titulo
   if request.GET["Titulo"]:
       tituloSolicitado = request.GET["Titulo"]
       documentos = Documento.objects.filter(
           contenido__icontains=tituloSolicitado)
       if len(documentos)!=0:
            return render(request, "Pares3/busqueda.html", {"documentos": documentos} )
       else:
           error="No se ha encontrado ningún documento con ese título"
           return render(request, "Pares3/busqueda.html", {"mensaje_busqueda": error} )
       return render(request, "Pares3/busqueda.html", {"documentos": documentos} )
    # Busqueda por siglo 
   if request.GET["Siglo"]:
       sigloSolicitado= request.GET["Siglo"]
       documentos = Documento.objects.filter(
           siglo__icontains=sigloSolicitado)
       if len(documentos)!=0:
            return render(request, "Pares3/busqueda.html", {"documentos": documentos} )
       else:
           error="No se ha encontrado ningún documento de ese siglo"
           return render(request, "Pares3/busqueda.html", {"mensaje_busqueda": error} ) 
   else:
       mensaje="No ha introducido ningún valor en los campos de búsqueda "
       return render(request, "Pares3/busqueda.html", {"mensaje_busqueda": mensaje} )

def detalleDocumento (request, signatura):
    detalleDocumento = Documento.objects.filter(
        signatura__icontains=signatura)
    return render(request, "Pares3/detalleDocumento.html", {"detalleDocumento": detalleDocumento} )

def verMisDocumentos (request, nombre): 
   
    lista= HistoriaUser.objects.filter(
        idusuario__nombre__icontains=nombre)

    nombre=request.session.get('nombre')
    email=request.session.get('email')
    a1=request.session.get('apellido1')
    a2=request.session.get('apellido2')
    tel=request.session.get('telefono')
    pais=request.session.get('pais')

    return render(request, "Pares3/perfil.html", { "lista": lista, 'nombre':nombre, 'email':email, 'pais':pais, 'tel': tel, 'a1':a1, 'a2':a2} )

def registrarUsuario (request):
    if request.POST["nombre"] and request.POST["1apellido"] and request.POST["2apellido"] and request.POST["telefono"]and request.POST["pais"]and request.POST["email"]and request.POST["pw"]:
        passIntroducido = request.POST["pw"]
        pwEncriptado=encriptar(passIntroducido)
        u=Usuario (nombre=request.POST["nombre"], apellido1 =request.POST["1apellido"], apellido2=request.POST["2apellido"], email=request.POST["email"], telefono=request.POST["telefono"], pais=request.POST["pais"],password=pwEncriptado)
        print(u.nombre)
        u.save()
        return redirect("home")
        
def guardarDoc (request,signatura):
    print(signatura)
    if request.session.get('nombre'):
        emailsesion=request.session.get('email')

        Usuario_sesion = Usuario.objects.filter(email__icontains=emailsesion)
        for i in Usuario_sesion:
            idU=request.session['user_id']=i.idUsusario
            
        historial=HistoriaUser(signatura_id=signatura, idusuario_id= idU)
        historial.save()
        detalleDocumento = Documento.objects.filter(
            signatura__icontains=signatura)
        mensajeCorrecto="Guardado correctamente  "

        return render(request, "Pares3/detalleDocumento.html", {"detalleDocumento": detalleDocumento, 'mensaje':mensajeCorrecto}  )
    else:
        mensaje="Debe registrarse para guardar el documento "
        return render(request, "Pares3/index.html", {'mensaje':mensaje})
    pass  


def Eliminar_historial_Doc (request, signatura):
    Eliminar_registro=HistoriaUser.objects.filter(
        signatura__signatura__icontains=signatura)
    Eliminar_registro.delete()    
    return redirect("home")
    
