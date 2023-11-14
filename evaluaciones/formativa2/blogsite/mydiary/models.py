from django.db import models
from django.utils import timezone

# Create your models here.
class Entry(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
    
