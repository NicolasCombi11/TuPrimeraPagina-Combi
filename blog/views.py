
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AuthorForm, CategoryForm, PostForm, PostSearchForm
from .models import Author, Category, Post
from django.db.models import Q

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            Author.objects.create(**form.cleaned_data)
            messages.success(request, 'Autor creado correctamente.')
            return redirect('author_create')
    else:
        form = AuthorForm()
    return render(request, 'author_form.html', {'form': form})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            messages.success(request, 'Categoría creada correctamente.')
            return redirect('category_create')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(
                titulo=form.cleaned_data['titulo'],
                contenido=form.cleaned_data['contenido'],
                autor=form.cleaned_data['autor'],
                categoria=form.cleaned_data['categoria']
            )
            messages.success(request, 'Post creado correctamente.')
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})

def post_list(request):
    posts = Post.objects.select_related('autor','categoria').order_by('-creado')
    return render(request, 'post_list.html', {'posts': posts})

def post_search(request):
    form = PostSearchForm(request.GET or None)
    results = []
    query = ''
    if form.is_valid():
        query = form.cleaned_data['q']
        results = Post.objects.filter(
            Q(titulo__icontains=query) | Q(contenido__icontains=query)
        ).select_related('autor','categoria').order_by('-creado')
    return render(request, 'search.html', {'form': form, 'results': results, 'query': query})
