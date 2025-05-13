import pytest

from src.vacancies import Vacancies


@pytest.fixture
def vacancy_data():
    return [{
        'name': 'Python Developer',
        'alternate_url': 'https://hh.ru/vacancy/123',
        'salary': 100000,
        'snippet': {'requirement': 'Опыт работы от 3 лет'}
    }]


@pytest.fixture
def vacancy_data_2():
    return [{
        'name': 'Junior Python',
        'alternate_url': 'https://hh.ru/vacancy/456',
        'salary': None,
        'snippet': {'requirement': 'Опыт работы от 2 лет'}
    }]


@pytest.fixture
def vacancy_creation():
    return Vacancies(
        name='Test',
        alternate_url='test.url',
        salary={'from': 50000},
        snippet={'requirement': 'Опыт работы от 3 лет'}
    )


@pytest.fixture
def vacancy_creation2():
    return Vacancies(
        name='Test',
        alternate_url='test.url',
        salary={'from': None},
        snippet={'requirement': 'Опыт работы от 3 лет'}
    )
