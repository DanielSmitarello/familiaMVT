from django.shortcuts import render
from familiares.models import Familiar
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def familiares(request): #cree la página
    contex = {
    }
    return render(request, "familiares.html", context=contex)

def index(request): #cree la página
    contex = {
        'date': datetime.now(),
    }
    return render(request, 'index.html', context = contex)

def mostrarfamily(request): #me crea el llamado del objeto que carga los datos de la sqlite
    integrantes = Familiar.objects.all()
    context = {
        'integrantes':integrantes
    }
    return render(request, "familiares.html", context = context)

def time(request):
    hora = datetime.now()
    context = {
        'hora': hora,
    }
    return render(request, 'familiares.html', context = context)
