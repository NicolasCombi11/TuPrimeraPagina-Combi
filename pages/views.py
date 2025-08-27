from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Page
from .forms import PageForm

def home(request):
    return HttpResponse("Bienvenido a Tu Primera Página 🚀")

class PageListView(ListView):
    model = Page
    template_name = 'pages/page_list.html'
    context_object_name = 'pages'
    ordering = ['-creado']

class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('pages:list')
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('pages:list')

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/page_confirm_delete.html'
    success_url = reverse_lazy('pages:list')

@login_required  # <- Decorador pedido en la consigna
def my_pages(request):
    qs = Page.objects.filter(autor=request.user).order_by('-creado')
    return render(request, 'pages/mine.html', {'pages': qs})