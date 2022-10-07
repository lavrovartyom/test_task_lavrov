from django.db import models


class Habr(models.Model):
	""" Модель постов с сайта Habr """

	title = models.TextField(verbose_name='Заголовок статьи')
	date = models.CharField(max_length=50, verbose_name='Дата создания')
	user_name = models.CharField(max_length=50, verbose_name='Имя пользователя')
	user_link = models.URLField(verbose_name='Ссылка на пользователя')
	objects = models.Manager()

	def __str__(self):
		return self.title
