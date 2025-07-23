from django.shortcuts import render
from .models import Post

def main_page(requers):
	'''Главная страница'''
	posts = Post.objects.all() # SELET * FROM DataBase			Импорт всей базы данных 
	data = {
		'title': 'Главная страница',
		'content': posts
	}
	return render(requers, 'news_app/index.html', data)