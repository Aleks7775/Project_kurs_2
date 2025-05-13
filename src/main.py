from src.api_hh import Api, HH
from src.vacancies import Vacancies
from src.working_files import Saver, JSONSaver
from src.utils import filter_salary_range, filter_keyword_vacancy, to_dict, new_job_vacancy
import os
import json

path_ = os.path.join('..', 'data', 'example.json')
record = JSONSaver()
examination = record.receiving_data(path_)

hh_api = HH()


def user_interaction():
    """Функция для получения данных от пользователя"""
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: ")) # по зарплате
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат от и до через пробел: ")

    hh = hh_api.get_vacancies(search_query, top_n)
    vacancy = Vacancies.hh_vacancies(hh)
    filter_vacancy = filter_keyword_vacancy(vacancy, filter_words)
    ranged_vacancies = filter_salary_range(filter_vacancy, salary_range)
    return to_dict(ranged_vacancies)


user_output = user_interaction()
for i in user_output:
    print(i)

print(hh_api.connect_to_api()) # проверка статус кода

new_job_vacancy(user_output, examination, record, path_) # запись результатов в файл
