from tkinter.tix import Tree
import uuid
from django.db import models
from django.urls import reverse
# Create your models here.

class Genero(models.Model):
    name = models.CharField(max_length=60, help_text='Genero de la pelicula')
    
    def __str__(self):
        return self.name

class Pelicula(models.Model):
    title = models.CharField(max_length=30)
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    resumen = models.TextField(max_length=140, help_text='De que va la pelicula')
    isbn = models.CharField('ISBN', max_length=13, help_text='ISBN de 13 caracteres')
    genre = models.ManyToManyField(Genero)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("pelicula_detail", args=[str(self.id)])
    
class PeliculaInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    pelicula = models.ForeignKey('Pelicula', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    
    def __str__(self):
        return '%s (%s)' % (self.id, self.pelicula.title)
    
    
class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacimiento = models.DateField(null=True, blank=True)
    muerte = models.DateField('Fallecido', null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse("autor_detail", args=[str(self.id)])
    
    def __str__(self):
        return '%s (%s)' % (self.apellido, self.nombre)
    