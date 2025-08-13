
from django.urls import path
from . import views

urlpatterns = [
    path('autores/nuevo/', views.author_create, name='author_create'),
    path('categorias/nueva/', views.category_create, name='category_create'),
    path('posts/nuevo/', views.post_create, name='post_create'),
    path('posts/', views.post_list, name='post_list'),
    path('buscar/', views.post_search, name='post_search'),
]
