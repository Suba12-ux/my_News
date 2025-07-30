from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main_page, name='page_main'),
    path('singin', user_login, name='page_singin'),
    path('singout', user_logout, name='page_singout'),
    path('registration', registration, name='page_regist'),
    path('add_post', PostAddForm, name='creat_post'),

] 

if settings.DEBUG: 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
