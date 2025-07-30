from django.shortcuts import render, redirect
from .models import Post
from .forms import PostAddForm, Login_form
from django.contrib.auth import login, logout

def main_page(request):
	'''Главная страница'''
	content_db1 = Post.objects.order_by('-pk').all() # ORM запрос		Импорт всей базы данных 
	content_db2 = Post.objects.order_by('photo').all() 
	text = {
		'title': 'Главная страница',
		'total': content_db1,
		'photo': content_db2
	}
	return render(request, 'news_app/index.html', text)


def registration(request):
	""" Регистрация """
	content_db2 = Post.objects.order_by('-pk')
	text = {
		'title': 'Регистрация',
		'total': content_db2,
	}
	return render(request, 'news_app/registration.html', text)

def add_post(request ):
	"""Создание поста не в админке"""
	if request.method  == 'POST':
		form = PostAddForm(request.POST, request.FILES)

		if form.is_valid():
			post = Post.objects.create(**form.cleaned_data)
			post.save()
			return redirect('page_main')
	else:
		form = PostAddForm()
		text = {
			'title': 'Создание статьи',
			'form': form,
		}

		return render(request, 'news_app/new_post.html', text)


def user_login(request):
	"""Вход ползоваетеля"""
	if request.method  == 'POST':
		form = Login_form(data=request.POST)

		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('page_main')
	else:
		form = Login_form()
		text = {
			'title': 'Вход',
			'form': form,
		}

		return render(request, 'news_app/singin.html', text)

def user_logout(request):
	'''Выход из профиля'''
	logout(request)
	return redirect('page_main')