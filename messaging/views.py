from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Message

@login_required
def inbox(request):
    # Obtener todos los mensajes donde el usuario es el remitente o el destinatario
    all_messages = Message.objects.filter(
        Q(sender=request.user) | Q(recipient=request.user)
    ).order_by('-timestamp')

    # Diccionario para almacenar la última conversación de cada usuario
    conversations = {}
    
    for message in all_messages:
        if message.sender == request.user:
            partner = message.recipient
        else:
            partner = message.sender

        if partner not in conversations:
            conversations[partner] = message

    # Convertir el diccionario a una lista de mensajes
    conversations_list = list(conversations.values())

    users = User.objects.all().exclude(username=request.user.username)

    return render(request, 'messaging/inbox.html', {
        'conversations': conversations_list,
        'users': users
    })


@login_required
def conversation(request, username):
    recipient = get_object_or_404(User, username=username)
    
    # Nueva consulta para recuperar todos los mensajes entre ambos usuarios
    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(recipient=recipient)) |
        (Q(sender=recipient) & Q(recipient=request.user))
    ).order_by('timestamp')

    # Marcar los mensajes como leídos
    unread_messages = messages.filter(recipient=request.user, is_read=False)
    for message in unread_messages:
        message.is_read = True
        message.save()

    return render(request, 'messaging/conversation.html', {
        'recipient': recipient,
        'messages': messages
    })

@login_required
def compose(request, username=None):
    if request.method == 'POST':
        recipient = get_object_or_404(User, username=request.POST.get('recipient'))
        body = request.POST.get('body')
        
        if body:
            Message.objects.create(sender=request.user, recipient=recipient, body=body)
            return redirect('messaging:conversation', username=recipient.username)

    users = User.objects.all().exclude(username=request.user.username)
    return render(request, 'messaging/compose.html', {'users': users})