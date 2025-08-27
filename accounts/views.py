from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm, UserEditForm, ProfileForm
from .models import Profile

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.get_or_create(user=user)
            login(request, user)
            messages.success(request, '¡Registro exitoso!')
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile(request):
    Profile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile.html')

@login_required
def profile_edit(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        uform = UserEditForm(request.POST, instance=request.user)
        pform = ProfileForm(request.POST, request.FILES, instance=profile)
        if uform.is_valid() and pform.is_valid():
            uform.save(); pform.save()
            messages.success(request, 'Perfil actualizado.')
            return redirect('profile')
    else:
        uform = UserEditForm(instance=request.user)
        pform = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_form.html', {'uform': uform, 'pform': pform})
