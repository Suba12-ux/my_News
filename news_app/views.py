from django.shortcuts import render, redirect
from .models import Post
from .forms import PostAddForm, Login_form, RegistrationForms
from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm as Login_form
from django.contrib.auth import login as auth_login

def main_page(request):
	'''Главная страница'''
	content_db1 = Post.objects.order_by('-pk').all() # ORM запрос		Импорт всей базы данных 
	text = {
		'title': 'Главная страница',
		'total': content_db1,
	}
	return render(request, 'news_app/index.html', text)

def registration(request):
    """Регистрация нового пользователя"""
    if request.method == 'POST':
        form = RegistrationForms(data=request.POST)
        
        if form.is_valid():
            try:
                user = form.save()
                messages.success(request, 'Регистрация прошла успешно! Теперь вы можете войти.')
                return redirect('page_singout')
            except Exception as e:
                messages.error(request, f'Произошла ошибка при регистрации: {str(e)}')
        else:
            # Добавляем ошибки формы в сообщения
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = RegistrationForms()
        context = {
            'title': 'Регистрация',
            'form': form,
        }
        return render(request, 'news_app/registration.html', context)

def add_post(request):
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

def del_post(request, title_name):
	"""Удаление поста не в админке"""
	post = Post.objects.get(title = title_name)
	post.delete()
	return redirect('page_main')

def user_login(request):
    """Вход пользователя"""
    if request.method == 'POST':
        form = Login_form(request, data=request.POST)  # Передаем request в форму
        
        if form.is_valid():
            try:
                user = form.get_user()
                remember_me = request.POST.get('remember_me') == 'on'
                
                # Используем auth_login вместо login (вы импортировали его как auth_login)
                auth_login(request, user)
                
                # Устанавливаем срок действия сессии
                if not remember_me:
                    request.session.set_expiry(0)  # Сессия закроется при закрытии браузера
                else:
                    # Установите желаемый срок для "запомнить меня" (например, 2 недели)
                    request.session.set_expiry(60 * 60 * 24 * 14)  # 14 дней
                
                messages.success(request, f"Добро пожаловать, {user.username}!")
                return redirect('page_main')
                
            except Exception as e:
                messages.error(request, f'Произошла ошибка при входе: {str(e)}')
        else:
            # Добавляем ошибки формы в сообщения
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{" ".join(field.split("_")).capitalize()}: {error}')
    else:
        form = Login_form(request)  # Передаем request в форму
    
    context = {
        'title': 'Вход',
        'form': form,
    }
    return render(request, 'news_app/singin.html', context)

def user_logout(request):
	'''Выход из профиля'''
	logout(request)
	return redirect('page_main')

