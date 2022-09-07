from django.shortcuts import render
from django.http import HttpResponseRedirect
from gestion_tareas.models import usuariosRegistrados,tarea
from django.urls import reverse

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
            return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))
        else:
            return render(request, 'gestion_tareas/login.html',{
                'mensaje':'Los datos ingresados son incorrectos',
            })
        #Fin de validación

    return render(request,'gestion_tareas/login.html')

def dashboard (request):
    #Filtrando tareas por alumnos
    usuario_id = []
    usuario_activo = usuariosRegistrados.objects.filter(codigoUsuario='1')
    for usuario in usuario_activo:
        usuario_id.append(usuario)
    usuario_responsable = tarea.objects.filter(usuarioResponsable='1')
    for usuario in usuario_responsable:
        usuario_id.append(usuario)
    #Fin del filtrado

    return render(request,'gestion_tareas/dashboard.html',{
        'objtareas': usuario_id,
    })

def creacionTareas (request):
    return render(request,'gestion_tareas/creacionTareas.html')

def edicionTareas (request):
    return render(request,'gestion_tareas/edicionTareas.html')

def vistaTareas (request):
    return render(request,'gestion_tareas/vistaTareas.html')