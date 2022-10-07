import requests
from bs4 import BeautifulSoup
from loguru import logger


def request_func(url: str) -> BeautifulSoup | bool:
	""" Функция, которая делает запросы к сайту """
	try:
		request = requests.get(url, timeout=30)
		if request.status_code == 200:
			soup = BeautifulSoup(request.text, 'lxml')
			return soup

	except requests.exceptions.RequestException as exc:
		logger.error(exc)
		return False
