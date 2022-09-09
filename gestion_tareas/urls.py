from . import views
from django.urls import path

app_name = 'gestion_tareas'

urlpatterns = [
    path('',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('creacionTareas',views.creacionTareas,name='creacionTareas'),
    path('edicionTareas/<str:ind>',views.edicionTareas,name='edicionTareas'),
    path('vistaTareas/<str:ind>',views.vistaTareas,name='vistaTareas'),
    path('eliminarTarea/<str:ind>',views.eliminarTarea,name='eliminarTarea'),
    path('finalizarTarea/<str:ind>',views.finalizarTarea,name='finalizarTarea'),
]