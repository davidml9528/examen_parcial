from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login (request):
    return HttpResponse('Pagina de login')

def dashboard (request):
    return HttpResponse('Aquí va el dashboard')