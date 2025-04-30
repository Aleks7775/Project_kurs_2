from src.api_hh import Api, HH



hh_api = HH()
vacancies = hh_api.get_vacancies("python")
print(vacancies)