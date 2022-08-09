from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    numerosPeliculas = Pelicula.objects.all().count()
    numeroAutores = Autor.objects.all().count()
    numeroGeneros = Genero.objects.all().count()
    
    return render(
        request,
        'index.html',
        context={
            'numero_peliculas': numerosPeliculas,
            'numero_autores': numeroAutores,
            'numero_generos': numeroGeneros,
        }
    )