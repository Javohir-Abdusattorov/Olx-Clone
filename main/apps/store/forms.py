
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
	username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control white-text',
        'placeholder': 'Enter username',
    }))

	email = forms.EmailField(widget=forms.TextInput(attrs={
		'type': 'email',
		'class': 'form-control white-text',
        'placeholder': 'Enter email',
	}))

	password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control white-text',
        'placeholder': 'Enter password',
    }))

	password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control white-text',
        'placeholder': 'Re-enter password',
    }))

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		exclude = []