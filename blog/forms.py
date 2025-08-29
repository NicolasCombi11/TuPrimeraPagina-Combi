
from django import forms
from .models import Author, Category, Post

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['nombre', 'email', 'bio']
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['nombre']

class PostForm(forms.Form):
    titulo = forms.CharField(max_length=120, label='Título')
    contenido = forms.CharField(widget=forms.Textarea, label='Contenido')
    autor = forms.ModelChoiceField(queryset=Author.objects.all(), label='Autor')
    categoria = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, label='Categoría')

class PostSearchForm(forms.Form):
    q = forms.CharField(max_length=120, label='Buscar por título o contenido')
