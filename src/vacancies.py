class Vacancies:
    """Класс для работы с вакансиями"""
    __slots__ = ('name', 'alternate_url', 'salary', 'snippet')

    def __init__(self, name, alternate_url, salary, snippet):
        self.name = name
        self.alternate_url = alternate_url
        self.salary = self.__validate_salary(salary.get('from') if salary else None)
        self.snippet = snippet.get('requirement', 'Описание не указано')

    def __validate_salary(self, salary):
        """Валидация зарплаты"""
        if salary is None:
            return 0
        try:
            return int(salary)
        except (ValueError, TypeError):
            return 0

    def __repr__(self):
        """Методы сравнения вакансий по зарплате"""
        return f"{self.name}, {self.alternate_url}, {self.salary}, {self.snippet}"

    def __lt__(self, other):
        """ меньше < """
        return self.salary < other.salary

    def __gt__(self, other):
        """больше >"""
        return self.salary > other.salary

    def __eq__(self, other):
        """равно =="""
        return self.salary == other.salary

    @classmethod
    def hh_vacancies(cls, vacancies_data):
        """Преобразовывает список словарей в список объектов Vacancy"""
        return [
            cls(
                name=i['name'],
                alternate_url=i['alternate_url'],
                salary=i['salary'],
                snippet=i['snippet']
            ) for i in vacancies_data
        ]
