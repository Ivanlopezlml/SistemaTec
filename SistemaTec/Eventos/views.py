from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Convocatoria
# Create your views here.


def Inicio(request):
    return render(request, 'Inicio.html')


def ConvocatoriaView(request):
    registros = Convocatoria.objects.all()
    return render(request, 'Convocatoria.html', {'registros': registros})


def add_teams(request):
    return render(request, 'form_add_teams.html')

    


