from django.urls import path

import AppEntrega.views


urlpatterns= [
    path('', AppEntrega.views.inicio, name="inicio"),
    path('about/', AppEntrega.views.nosotros, name="Nosotros"),
    path('contacto/', AppEntrega.views.contacto, name="contacto"),
]