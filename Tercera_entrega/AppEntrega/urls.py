from django.urls import path
from AppEntrega import views

urlpatterns= [
    path('', views.inicio, name="inicio"),
    path('pasajero', views.pasajero, name="pasajero"),
    path('destinos', views.destinos, name="destinos"),
    path('formularioSorteo', views.sorteo, name="formulariosSorteo")
]
