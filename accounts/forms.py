from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar','bio','link','birthdate')
        widgets = {'bio': forms.Textarea(attrs={'rows':3})}
