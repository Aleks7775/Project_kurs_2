import pytest
from src.vacancies import Vacancies


def test_vacancies_init(vacancy_creation):
    """Тест инициализации"""
    assert vacancy_creation.name == "Test"
    assert vacancy_creation.alternate_url == "test.url"
    assert vacancy_creation.salary == 50000
    assert vacancy_creation.snippet == "Опыт работы от 3 лет"


def test_salary_validation(vacancy_creation, vacancy_creation2):
    """Тест валидации и сравнения"""
    v1 = vacancy_creation
    assert v1.salary == 50000
    v2 = vacancy_creation2
    assert v2.salary == 0

    assert v1 > v2
    assert v2 < v1


def test_hh_vacancies_classmethod(vacancy_data_2):
    """Тест classmethod для создания списка вакансий"""
    vacancies = Vacancies.hh_vacancies(vacancy_data_2)

    assert len(vacancies) == 1
    assert isinstance(vacancies[0], Vacancies)
    assert vacancies[0].name == 'Junior Python'
    assert vacancies[0].snippet == 'Опыт работы от 2 лет'
