import time
from request_habr import request_func
from models import HabrModel, DATABASES
from loguru import logger


def main() -> None:
	""" Основная функция, которая принимает и обрабатывает запросы, а также производит записи в базу дынных """
	while True:
		response = request_func('https://habr.com/ru/all/page1/')
		if response:
			hub_list = response.findAll('a', class_='tm-article-snippet__title-link')

			for i_link in hub_list:
				link = f'https://habr.com{i_link.get("href")}'
				info_hub = request_func(link)
				if info_hub:
					try:
						title = info_hub.find('h1', class_='tm-article-snippet__title tm-article-snippet__title_h1').find('span').text
						date = info_hub.find('span', class_='tm-article-snippet__datetime-published').find('time').get('title')
						user_name = info_hub.find('span', class_='tm-user-info__user').text.strip()
						user_link = f'https://habr.com{info_hub.find("a", class_="tm-user-info__username").get("href")}'
					except AttributeError as exc:
						logger.error(exc)
						continue

					with DATABASES:
						HabrModel.create_table()
						rec = HabrModel.select().where(HabrModel.title == title)
						if not rec:
							HabrModel.create(title=title, date=date, user_name=user_name, user_link=user_link)
					print(
						f'Заголовок статьи: {title}'
						f'\nДата создания: {date}'
						f'\nИмя пользователя: {user_name}'
						f'\nСсылка на пользователя: {user_link}\n'
					)
				else:
					logger.error('Ошибка данных')
					continue
		else:
			logger.error('Ошибка запроса')
		time.sleep(600)


if __name__ == '__main__':
	logger.add('logs.log', format='{time} {level} {message}', level='DEBUG')
	logger.info('Старт программы')
	main()
