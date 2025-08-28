
from django.db import models

class Author(models.Model):
    nombre = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Category(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=120)
    subtitulo = models.CharField(max_length=200, blank=True, null=True)
    contenido = models.TextField()
    autor = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    categoria = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    imagen = models.ImageField(upload_to='post_images/', blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
