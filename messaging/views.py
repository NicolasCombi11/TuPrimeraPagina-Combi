from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from .forms import MessageForm

@login_required
def inbox(request):
    msgs = Message.objects.filter(recipient=request.user).order_by('-created')
    return render(request, 'messaging/inbox.html', {'messages_': msgs})

@login_required
def outbox(request):
    msgs = Message.objects.filter(sender=request.user).order_by('-created')
    return render(request, 'messaging/outbox.html', {'messages_': msgs})

@login_required
def compose(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            return redirect('messaging:outbox')
    else:
        form = MessageForm()
    return render(request, 'messaging/compose.html', {'form': form})

@login_required
def detail(request, pk):
    msg = get_object_or_404(Message, pk=pk)
    if msg.recipient == request.user and not msg.read:
        msg.read = True
        msg.save()
    return render(request, 'messaging/detail.html', {'msg': msg})
