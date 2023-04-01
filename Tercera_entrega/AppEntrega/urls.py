from django.urls import path

import AppEntrega.views
from AppEntrega.views import inicio

urlpatterns= [
    path('', AppEntrega.views.inicio, name="inicio"),
    #path('pasajero', pasajero, name="pasajero"),
  #  path('destinos', destinos, name="destinos"),
  #  path('formularioSorteo', sorteo, name="formulariosSorteo")
  #  path('reserva', reserva, name="formularioReserva")
]
