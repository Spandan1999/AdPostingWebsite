from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import AdPostModel


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widget = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class AdPostForm(forms.ModelForm):
    class Meta:
        model = AdPostModel
        fields = ['ad_type', 'ad_title', 'ad_description', 'contact_info', 'address', 'price']
        widget = {
            'ad_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Ad Type'}),
            'ad_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Ad Title'}),
            'ad_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Ad Description'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Contact Info'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Price'}),
        }
