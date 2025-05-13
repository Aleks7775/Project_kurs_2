import json
from typing import List


def filter_keyword_vacancy(vacancy, word) -> List[dict]:
    """Получение вакансий по ключевому слову"""
    word_list = []
    for i in vacancy:
        for key in word:
            if key.lower() in i.snippet.lower():
                word_list.append(i)
    return word_list


def filter_salary_range(filter_vacancy, salary_range) -> List[dict]:
    """функция считает диапазон зарплат от и до"""
    list_ = []
    for i in filter_vacancy:
        if int(min(salary_range.split())) <= i.salary <= int(max(salary_range.split())):
            list_.append(i)
    return list_


def to_dict(filtered) -> List[dict]:
    """Функция преобразует ответ пользователя в читаемы формат"""
    filtered_json = []
    for i in filtered:
        filtered_json.append({'название вакансии': i.name,
                              'ссылка на вакансию': i.alternate_url,
                              'зарплата': i.salary,
                              'требования': i.snippet})
    return filtered_json


def new_job_vacancy(dict_, examination, record, path_):
    """Добавление новых вакансий в файл без использовании дублей"""
    if len(examination) == 0:
        return record.add_vacancy(path_, dict_)
    else:
        new_job = json.loads(examination)
        for i in dict_:
            if i not in new_job:
                new_job.append(i)
        return record.add_vacancy(path_, new_job)
