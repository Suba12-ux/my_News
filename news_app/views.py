from django.shortcuts import render
from .models import Post

def main_page(requers):
	'''Главная страница'''
	content_db = Post.objects.values('title') # ORM запрос		Импорт всей базы данных 
	text = {
		'title': 'Главная страница',
		'total': content_db,
	}
	return render(requers, 'news_app/index.html', text)