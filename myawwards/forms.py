from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project,Profile
from pyuploadcare.dj.forms import ImageField

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'profile_pic', 'bio', 'contact']

class PostForm(forms.ModelForm):
    image = ImageField(label='')
    class Meta:
        model = Project
        fields = ['title', 'image', 'url', 'description']
