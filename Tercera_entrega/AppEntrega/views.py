from django.shortcuts import render
from django.http import HttpResponse
from AppEntrega.models import Pasajero
#from forms import Pasajeroform

# Create your views here.

def inicio(request):
    return render(request, 'index.html')

#def pasajero(request):
#    if request.method == "POST":
#        mi_formulario = Pasajeroform(request.POST)

#        if mi_formulario.is_valid():
#            informacion = mi_formulario.cleaned_data
#            alfajor_save = Alfajor(
#                nombre=informacion['nombre'],
#                tipo=informacion['tipo'],
#                sabor=informacion['sabor'],
#            )
 #           alfajor_save.save()

#    all_alfajores = Alfajor.objects.all()
    #context = {
#       "alfajores": all_al


#def pasajero(request):
#    context={
#        "form": form.Pasajeroform()
#    }
#    return render(request, 'AppEntrega/formulariopasajero.html', context=context)





#def sorteo(request):
#    return render(request,"AppEntrega/formularioSorteo.html")