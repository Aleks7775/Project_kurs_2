import requests
from abc import ABC, abstractmethod


class Api(ABC):

    @abstractmethod
    def connect_to_api(self):
        pass

    @abstractmethod
    def get_vacancies(self, keyword, per_page):
        pass


class HH(Api):
    """Абстрактный класс для работы с API сервиса"""
    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__params = {'text': '', 'page': 0, 'per_page': 10}

    def connect_to_api(self):
        """Метод подключения к API"""
        try:
            response = requests.get(self.__url)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise Exception(f"Ошибка подключения: {e}")

    def get_vacancies(self, keyword, per_page):
        """Метод преобразования ответа с АПИ в Python объект"""
        self.connect_to_api()
        self.__params['text'] = keyword
        self.__params['per_page'] = per_page

        try:
            response = requests.get(self.__url, self.__params)
            response.raise_for_status()
            data = response.json()
            return data.get('items', [])
        except requests.exceptions.RequestException as e:
            raise Exception(f"Ошибка получения вакансий: {e}")
