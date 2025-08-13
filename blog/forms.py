
from django import forms
from .models import Author, Category, Post

class AuthorForm(forms.Form):
    nombre = forms.CharField(max_length=80, label='Nombre')
    email = forms.EmailField(label='Email')
    bio = forms.CharField(widget=forms.Textarea, required=False, label='Bio')

class CategoryForm(forms.Form):
    nombre = forms.CharField(max_length=50, label='Nombre')
    descripcion = forms.CharField(widget=forms.Textarea, required=False, label='Descripción')

class PostForm(forms.Form):
    titulo = forms.CharField(max_length=120, label='Título')
    contenido = forms.CharField(widget=forms.Textarea, label='Contenido')
    autor = forms.ModelChoiceField(queryset=Author.objects.all(), label='Autor')
    categoria = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, label='Categoría')

class PostSearchForm(forms.Form):
    q = forms.CharField(max_length=120, label='Buscar por título o contenido')
