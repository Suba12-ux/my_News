from django.shortcuts import render
from .models import Post

def main_page(requers):
	'''Главная страница'''
	content_db1 = Post.objects.order_by('-pk').all() # ORM запрос		Импорт всей базы данных 
	content_db2 = Post.objects.order_by('photo').all() 
	text = {
		'title': 'Главная страница',
		'total': content_db1,
		'photo': content_db2
	}
	return render(requers, 'news_app/index.html', text)


def galary(requers):
	'''Галерея'''
	content_db2 = Post.objects.order_by('-pk')
	text = {
		'title': 'Галерея',
		'total': content_db2,
	}
	return render(requers, 'news_app/galary', text)



def singin(requers):
	content_db2 = Post.objects.order_by('-pk')
	text = {
		'title': 'Вход',
		'total': content_db2,
	}
	return render(requers, 'news_app/singin.html', text)


def registration(requers):
	""" Регистрация """
	content_db2 = Post.objects.order_by('-pk')
	text = {
		'title': 'Регистрация',
		'total': content_db2,
	}
	return render(requers, 'news_app/registration.html', text)

