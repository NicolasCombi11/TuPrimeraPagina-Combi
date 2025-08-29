
from django.contrib import admin
from .models import Author, Category, Post

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','email')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'fecha_publicacion') 
    list_filter = ('autor', 'categoria', 'fecha_publicacion')
    search_fields = ('titulo', 'contenido')
