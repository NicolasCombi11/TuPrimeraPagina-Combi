
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

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
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='post_images/', blank=True, null=True) 
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo
