from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

#++
class Post(models.Model):
    title = models.CharField(max_length=250) #charfield, signfiica un campo de caracteres
    content = models.TextField() #el textfiel,es un campo de texto mas grande, para escribir mas contenido 

    def __str__(self):
        return self.title #Esto es para colocarle de titulo lo que colocamos en el admin, cuando agregamos
#+

