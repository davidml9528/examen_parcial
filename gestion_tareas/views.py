from django.shortcuts import render
from django.http import HttpResponseRedirect
from gestion_tareas.models import usuariosRegistrados,tarea
from django.urls import reverse
from dateutil.parser import parse
from datetime import date,datetime

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
    if request.method == 'POST' :
        crear_fechaEntrega = request.POST.get('crear_fechaEntrega')
        crear_fechaEntrega = parse(crear_fechaEntrega)
        crear_descripcion= request.POST.get('crear_descripcion')
        crear_usuarioResponsable= request.POST.get('crear_usuarioResponsable')
        tarea(descripcion=crear_descripcion,fechaEntrega=crear_fechaEntrega,usuarioResponsable=crear_usuarioResponsable).save()
        return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))
    return render(request,'gestion_tareas/creacionTareas.html')

def edicionTareas (request,ind):
    tarea_editar = tarea.objects.get(id=ind)
    if request.method == 'POST':
        fecha = request.POST.get('crear_fechaEntrega')
        descrip = request.POST.get('crear_descripcion')
        usuarioRespo = request.POST.get('crear_usuarioResponsable')
        tarea_editar.fechaEntrega = fecha
        tarea_editar.descripcion = descrip
        tarea_editar.usuarioResponsable = usuarioRespo
        tarea_editar.save()
        return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))
    return render(request,'gestion_tareas/edicionTareas.html',{
        'tarea_info': tarea_editar,
    })

def vistaTareas (request,ind):
    tarea_editar = tarea.objects.get(id=ind)
    if request.method == 'POST':
        fecha = request.POST.get('crear_fechaEntrega')
        descrip = request.POST.get('crear_descripcion')
        usuarioRespo = request.POST.get('crear_usuarioResponsable')
        tarea_editar.fechaEntrega = fecha
        tarea_editar.descripcion = descrip
        tarea_editar.usuarioResponsable = usuarioRespo
        tarea_editar.save()
        return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))
    return render(request, 'gestion_tareas/vistaTareas.html', {
        'tarea_info': tarea_editar,
    })

def eliminarTarea (request,ind):
    tarea_editar = tarea.objects.get(id=ind)
    if request.method == 'POST':
        fecha = request.POST.get('crear_fechaEntrega')
        descrip = request.POST.get('crear_descripcion')
        usuarioRespo = request.POST.get('crear_usuarioResponsable')
        tarea_editar.fechaEntrega = datetime.strptime(str(fecha),'%Y-%m-%d')
        tarea_editar.descripcion = descrip
        tarea_editar.usuarioResponsable = usuarioRespo
        tarea_editar.delete()
        return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))
    return render(request, 'gestion_tareas/eliminarTarea.html', {
        'tarea_info': tarea_editar,
    })