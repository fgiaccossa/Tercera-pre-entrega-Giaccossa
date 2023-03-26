from django.urls import path
from AppEntrega import views

urlpatterns= [
    path('', views.inicio),
    path('cursos', views.cursos, name="cursos"),
    path('profesores', views.profesores),
    path('entregables', views.entregables),
]
