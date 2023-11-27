from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    # Campos del modelo
    nombre = models.CharField(max_length=200)

    # Función estándar para presentar info
    def __str__(self):
        return self.nombre


class Hashtag(models.Model):
    # Campos del modelo
    nombre = models.CharField(max_length=200)

    # Función estándar para presentar info
    def __str__(self):
        return self.nombre
    

class Post (models.Model):
    # Campos del modelo
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)

    # Relaciones con otros modelos
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)
    etiquetas = models.ManyToManyField(Hashtag)

    # Función estándar para presentar info
    def __str__(self):
        return self.titulo
