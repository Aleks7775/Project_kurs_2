import requests
from abc import ABC, abstractmethod


class Api(ABC):

    @abstractmethod
    def connect_to_api(self):
        pass

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HH(Api):
    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__params = {'text': '', 'page': 0, 'per_page': 1}


    def connect_to_api(self):
        try:
            response = requests.get(self.__url)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            raise Exception(f"Ошибка подключения: {e}")


    def get_vacancies(self, keyword):
        self.connect_to_api()
        self.__params['text'] = keyword

        try:
            response = requests.get(self.__url, params=self.__params)
            response.raise_for_status()
            data = response.json()
            return data.get('items', [])
        except requests.exceptions.RequestException as e:
            raise Exception(f"Ошибка получения вакансий: {e}")


    # def connect_to_api(self):
    #     response = requests.get(self.__url)
    #     if response.status_code != 200:
    #         raise Exception("Не удалось подключиться к API")
    #     return True
    #
    #
    # def get_vacancies(self, keyword):
    #     self.connect_to_api()  # Проверяем подключение перед запросом
    #     self.params['text'] = keyword
    #     response = requests.get(self.__url, self.params)
    #     return response.json()


# hh_api = HH()
# vacancies = hh_api.get_vacancies("python")
# print(vacancies)


# def connect_to_api(self):
#     try:
#         response = requests.get(self.base_url)
#         response.raise_for_status()  # Проверяет статус-код
#         return True
#     except requests.exceptions.RequestException as e:
#         raise Exception(f"Ошибка подключения: {e}")
#
#
# def get_vacancies(self, keyword):
#     self.connect_to_api()
#     self.params['text'] = keyword
#
#     try:
#         response = requests.get(self.base_url, params=self.params)
#         response.raise_for_status()
#         data = response.json()
#         return data.get('items', [])  # Возвращаем список вакансий
#     except requests.exceptions.RequestException as e:
#         raise Exception(f"Ошибка получения вакансий: {e}")


"""Создан класс для работы с hh.ru.
Класс для работы с hh.ru наследуется от абстрактного.
Реализованы все методы абстрактного класса.
Атрибуты экземпляра класса — приватные.
Метод подключения к API hh.ru — приватный.
В методе подключения к API отправляется запрос на базовый URL.
В методе подключения к API происходит проверка статус-кода ответа.
Метод подключения к API hh.ru вызывается в методе получения данных перед отправкой запроса.
Метод получения данных принимает параметр — ключевое слово для поиска вакансий.
Метод получения данных формирует параметры для запроса как минимум из text, per_page.
Метод получения данных отправляет запрос на API hh.ru для получения данных о вакансиях по ключевому слову.
Метод получения данных собирает данные ответа в формате списка словарей из ключа item. """

#
# class HH(Parser):
#     """
#     Класс для работы с API HeadHunter
#     Класс Parser является родительским классом, который вам необходимо реализовать
#     """
#
#     def __init__(self, file_worker):
#         self.url = 'https://api.hh.ru/vacancies'
#         self.headers = {'User-Agent': 'HH-User-Agent'}
#         self.params = {'text': '', 'page': 0, 'per_page': 100}
#         self.vacancies = []
#         super().__init__(file_worker)
#
#     def load_vacancies(self, keyword):
#         self.params['text'] = keyword
#         while self.params.get('page') != 20:
#             response = requests.get(self.url, headers=self.headers, params=self.params)
#             vacancies = response.json()['items']
#             self.vacancies.extend(vacancies)
#             self.params['page'] += 1

"""Класс должен уметь подключаться к API и получать вакансии."""
"""Абстрактный метод (def) определяет интерфейс, который должны реализовать все классы, наследующие от класса"""


#params = {"text": "python"}
# params = {'text': '', 'page': 0, 'per_page': 5}
# vacancies = requests.get("https://api.hh.ru/vacancies", params=params).json()
#
# page = vacancies["items"]
# for i in page:
#     print(i)


# url_get = "https://api.hh.ru/vacancies"
# response = requests.get(url_get) # отправка GET-запроса
# print(response.status_code) #<Response [200]>