from . import views
from django.urls import path

app_name = 'gestion_tareas'

urlpatterns = [
    path('',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('creacionTareas',views.creacionTareas,name='creacionTareas'),
    path('vistaTareas',views.vistaTareas,name='vistaTareas'),
    path('edicionTareas/<str:ind>',views.edicionTareas,name='edicionTareas'),
]