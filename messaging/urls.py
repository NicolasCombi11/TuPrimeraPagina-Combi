from django.urls import path
from . import views
from .views import MessageDeleteView


app_name = 'messaging'
urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('compose/', views.compose, name='compose'),
    path('<str:username>/', views.conversation, name='conversation'),
    path('delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
]
