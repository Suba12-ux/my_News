from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=255, verbose_name='Название')
	content = models.TextField(default='Основной текст поста.', verbose_name='Текст')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время поста')
	updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
	photo = models.ImageField(upload_to='Photos/', blank=True, null=True, verbose_name='Фото') # не обязательно для заполнения.
	watched = models.IntegerField(default=0, verbose_name='Просмотры')
	is_published = models.BooleanField(default=True, verbose_name='Видимость')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'