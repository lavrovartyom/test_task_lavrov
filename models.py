from peewee import CharField, SqliteDatabase, Model
import os

PATH_DB = os.path.abspath('my_test/db.sqlite3')
DATABASES = SqliteDatabase(PATH_DB)


class BaseModel(Model):

	class Meta:
		database = DATABASES


class HabrModel(BaseModel):
	title = CharField(max_length=300, verbose_name='Заголовок статьи')
	date = CharField(max_length=50, verbose_name='Дата создания')
	user_name = CharField(max_length=50, verbose_name='Имя пользователя')
	user_link = CharField(max_length=50, verbose_name='Ссылка на пользователя')

	class Meta:
		db_table = 'test_app_habr'
