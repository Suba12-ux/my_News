from django import forms
from .models import Post
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class PostAddForm(forms.ModelForm):
	"""Модель для создания постов пользователей"""
	class Meta:
		"""Ахитектура класса, наследуется от самого себя"""
		model = Post 
		fields = ['title', 'content', 'photo']


class Login_form(AuthenticationForm):
	"""Аутентификация пользователя"""
	username = forms.CharField(	label = 'Имя пользователя', max_length = 150)
	password = forms.CharField(	label = 'Имя пользователя', widget=forms.PasswordInput(attrs={'class': 'form-control'}))