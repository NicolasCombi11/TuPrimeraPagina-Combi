from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Page(models.Model):
    titulo = models.CharField(max_length=120)
    bajada = models.CharField(max_length=200, blank=True)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='pages/', blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo
