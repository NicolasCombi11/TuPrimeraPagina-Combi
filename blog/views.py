
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AuthorForm, CategoryForm, PostForm, PostSearchForm
from .models import Author, Category, Post
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor creado correctamente.')
            return redirect('post_create')
    else:
        form = AuthorForm()
    return render(request, 'blog/author_form.html', {'form': form})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada correctamente.')
            return redirect('post_create')
    else:
        form = CategoryForm()
    return render(request, 'blog/category_form.html', {'form': form})

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
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'autor', 'categoria']
    success_url = reverse_lazy('pages') 

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'autor', 'categoria']
    success_url = reverse_lazy('posts')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('posts')
    
    
def posts(request):
    posts_list = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': posts_list})


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'