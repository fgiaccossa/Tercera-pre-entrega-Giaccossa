from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(rquest):
    return HttpResponse('vista inicio')

def cursos(request):
    return HttpResponse('vista cursos')

def profesores(request):
    return HttpResponse('vista profesores')

def estudiantes(request):
    return HttpResponse('vista estudiantes')

def entregables(request):
    return HttpResponse('vista entregables')