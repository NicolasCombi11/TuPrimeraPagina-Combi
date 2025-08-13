
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
    list_display = ('id','titulo','autor','categoria','creado')
    search_fields = ('titulo','contenido')
    list_filter = ('categoria','autor')
