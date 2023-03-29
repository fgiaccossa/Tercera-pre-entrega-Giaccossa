from django.urls import path
from AppEntrega import views

urlpatterns= [
    path('', views.inicio, name="inicio"),
    path('cursos', views.cursos, name="cursos"),
    path('profesores', views.profesores, name="profesores"),
    path('entregables', views.entregables, name="entregables"),
]
