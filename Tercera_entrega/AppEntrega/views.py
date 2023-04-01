from django.shortcuts import render
from django.http import HttpResponse

import AppEntrega.forms
from AppEntrega.forms import Contacto
from AppEntrega.models import Pasajero
#from forms import Pasajeroform

# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'about.html')

def contacto (request):
    if request.method == "POST":

        form = AppEntrega.forms.Contacto(request.POST)
        if form.is_valid():
            form.save()

            return redirect("AppEntrega_inicio")





#def sorteo(request):
#    return render(request,"AppEntrega/formularioSorteo.html")