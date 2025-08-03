from django import forms
from .models import Post
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.forms import User


class PostAddForm(forms.ModelForm):
	"""Модель для создания постов пользователей"""
	class Meta:
		"""Ахитектура класса, наследуется от самого себя"""
		model = Post 
		fields = ['title', 'content', 'photo']



class Login_form(AuthenticationForm):
	"""Аутентификация пользователя"""
	username = forms.CharField(	label = 'Имя пользователя', max_length = 150)
	password = forms.CharField(	label = 'Пароль пользователя', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegistrationForms(UserCreationForm):
	"""Форма регистрации"""
	class Meta:
		model = User 
		fields = ('username', 'email', 'password1', 'password2')

	#username = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
	#email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'umail@'}))
	#password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
	#password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтверждение пароля'}))