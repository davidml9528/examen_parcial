from django.shortcuts import render
from django.http import HttpResponse
from gestion_tareas.models import usuariosRegistrados,tarea

# Create your views here.
def login (request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        passwordUsuario = request.POST.get('passwordUsuario')
        #Validacion de información
        usuario_registrado = 0
        usuarios_totales = usuariosRegistrados.objects.all()

        for estudiante in usuarios_totales:
            if estudiante.nombre == nombreUsuario and estudiante.password == passwordUsuario:
                usuario_registrado = 1
        if usuario_registrado == 1:
            return render(request, 'gestion_tareas/dashboard.html')
        else:
            return render(request, 'gestion_tareas/login.html',{
                'mensaje':'Los datos ingresados son incorrectos',
            })
        #Fin de validación

    return render(request,'gestion_tareas/login.html')

def dashboard (request):
    return render(request,'gestion_tareas/dashboard.html')

def creacionTareas (request):
    return render(request,'gestion_tareas/creacionTareas.html')

def edicionTareas (request):
    return render(request,'gestion_tareas/edicionTareas.html')

def vistaTareas (request):
    return render(request,'gestion_tareas/vistaTareas.html')