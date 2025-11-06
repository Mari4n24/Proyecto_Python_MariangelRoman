from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    # return HttpResponse("<h1>Hola soy el proyecto</h1>") 
    return render(request, "inicio.html")

def about(request):
    return render(request, "about.html")