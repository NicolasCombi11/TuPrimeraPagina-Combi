from django.urls import path
from . import views
app_name = 'messaging'
urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('enviados/', views.outbox, name='outbox'),
    path('nuevo/', views.compose, name='compose'),
    path('<int:pk>/', views.detail, name='detail'),
]
