from django.shortcuts import render
from django.http import HttpResponse
#from forms import pasajero

# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def pasajero(request):
    return render(request)
def destinos(request):
    return render(request,'AppEntrega/destinos.html')

def preferencias(request):
    return HttpResponse('vista preferencias')

def sorteo(request):
    return render(request,"AppEntrega/formularioSorteo.html")