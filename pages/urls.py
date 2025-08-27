from django.urls import path
from . import views
from .views import (
    PageListView, PageDetailView,
    PageCreateView, PageUpdateView, PageDeleteView,
    my_pages
)
app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),
    path('', PageListView.as_view(), name='list'),
    path('mias/', my_pages, name='mine'),
    path('nueva/', PageCreateView.as_view(), name='create'),
    path('<int:pk>/', PageDetailView.as_view(), name='detail'),
    path('<int:pk>/editar/', PageUpdateView.as_view(), name='update'),
    path('<int:pk>/borrar/', PageDeleteView.as_view(), name='delete'),
]
