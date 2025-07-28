from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main_page, name='page_main'),
    path('photos', galary, name='page_photo'),
    path('singin', singin, name='page_singin'),
    path('registration', registration, name='page_regist'),
] 

if settings.DEBUG: 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
