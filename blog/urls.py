
from django.urls import path
from . import views
from .views import PostCreateView, PostUpdateView, PostDeleteView, PostDetailView

urlpatterns = [
    path('', views.post_list, name='pages'),
    path('autores/nuevo/', views.author_create, name='author_create'),
    path('categorias/nueva/', views.category_create, name='category_create'),
    path('buscar/', views.post_search, name='post_search'),
    path('posts/nuevo/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/editar/', PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/eliminar/', PostDeleteView.as_view(), name='post_delete'),
    path('posts/', views.post_list, name='post_list'),

]
