from django.urls import path
from . import views
app_name = 'messaging'
urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('compose/', views.compose, name='compose'),
    path('<str:username>/', views.conversation, name='conversation'),
]
