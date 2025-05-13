import pytest
import json
import os
from unittest.mock import mock_open, patch
from src.working_files import JSONSaver

# Тестовые данные
test_data = [{'name': 'Python Dev', 'salary': 100000}]
test_json = json.dumps(test_data, ensure_ascii=False, indent=4)


@patch('builtins.open', new_callable=mock_open)
@patch('json.dump')
def test_add_vacancy_success(mock_dump, mock_file):
    saver = JSONSaver()
    result = saver.add_vacancy('test.json', test_data)

    mock_file.assert_called_once_with('test.json', 'w')
    mock_dump.assert_called_once_with(test_data, mock_file(), ensure_ascii=False, indent=4)
    assert result == "Файл добавлен"


@patch('builtins.open', side_effect=FileNotFoundError)
def test_receiving_data_file_not_found(mock_file):
    """Тест обработки отсутствия файла"""
    saver = JSONSaver()
    result = saver.receiving_data('missing.json')

    assert result == "Файл отсутствует"


@patch('builtins.open', mock_open(read_data=test_json))
def test_receiving_data_success():
    """Тест успешного чтения файла"""
    saver = JSONSaver()
    result = saver.receiving_data('test.json')

    open.assert_called_once_with('test.json', 'r', encoding='utf-8')
    assert result == test_json
