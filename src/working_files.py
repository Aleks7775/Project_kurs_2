from abc import ABC, abstractmethod
import json
import os
from typing import List, Dict, Union


path_ = os.path.join('..', 'data', 'example.json')


class Saver(ABC):
    """Класс для работы с файлами"""

    @abstractmethod
    def receiving_data(self, file):
        pass

    @abstractmethod
    def add_vacancy(self, path, file):
        pass

    @abstractmethod
    def delete_vacancy(self, file):
        pass


class JSONSaver(Saver):
    def add_vacancy(self, path, file) -> str:
        """ добавления данных в файл"""
        with open(path, 'w') as f:
            json.dump(file, f, ensure_ascii=False, indent=4)
            return "Файл добавлен"

    def receiving_data(self, file) -> str:
        """ получения данных из файла """
        try:
            with open(file, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return "Файл отсутствует"

    def delete_vacancy(self, file) -> str:
        """ удаления данных из файла"""
        with open(file, 'r+') as f:
            f.truncate(0)
            return "Файл очищен"
