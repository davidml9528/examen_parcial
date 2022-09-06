from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login (request):
    return render(request,'gestion_tareas/login.html')

def dashboard (request):
    return HttpResponse('Aquí va el dashboard')