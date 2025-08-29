from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Message

@login_required
def inbox(request):
    # Obtener el último mensaje para cada conversación
    # Esta es una manera más robusta de hacer la consulta en SQLite
    latest_messages = {}
    messages = Message.objects.filter(
        Q(sender=request.user) | Q(recipient=request.user)
    ).order_by('timestamp') # Ordenamos por fecha para obtener el último mensaje

    for message in messages:
        if message.sender == request.user:
            partner = message.recipient
        else:
            partner = message.sender
        latest_messages[partner] = message # Sobrescribe hasta encontrar el más reciente

    # Convertir el diccionario en una lista de mensajes
    conversations_list = list(latest_messages.values())

    users = User.objects.all().exclude(username=request.user.username)

    return render(request, 'messaging/inbox.html', {
        'conversations': conversations_list,
        'users': users
    })

    
    
@login_required
def conversation(request, username):
    recipient = get_object_or_404(User, username=username)

    # Consulta corregida para obtener todos los mensajes entre los dos usuarios
    messages = Message.objects.filter(
        Q(sender=request.user, recipient=recipient) |
        Q(sender=recipient, recipient=request.user)
    ).order_by('timestamp')

    # Marcar los mensajes no leídos como leídos
    unread_messages = messages.filter(recipient=request.user, is_read=False)
    for message in unread_messages:
        message.is_read = True
        message.save()
        
    if request.method == 'POST':
        body = request.POST.get('body')
        if body:
            Message.objects.create(sender=request.user, recipient=recipient, body=body)
        return redirect('messaging:conversation', username=recipient.username)

    return render(request, 'messaging/conversation.html', {
        'recipient': recipient,
        'messages': messages
    })


@login_required
def compose(request):
    if request.method == 'POST':
        recipient_username = request.POST.get('recipient')
        body = request.POST.get('body')
        
        recipient = get_object_or_404(User, username=recipient_username)

        if body:
            Message.objects.create(sender=request.user, recipient=recipient, body=body)
            # Redireccionamiento corregido
            return redirect('messaging:conversation', username=recipient.username)

    users = User.objects.all().exclude(username=request.user.username)
    return render(request, 'messaging/compose.html', {'users': users})

class MessageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Message
    template_name = 'messaging/message_confirm_delete.html'
    success_url = reverse_lazy('messaging:inbox')

    def test_func(self):
        message = self.get_object()
        return self.request.user == message.sender