import pytest

from src.api_hh import HH
from unittest.mock import Mock, patch
import requests


@patch('requests.get')
def test_api(mock_get):
    mock_get.return_value.json.return_value = {'items': [{'id': 1}]}
    mock_get.return_value.status_code = 200

    response = requests.get('url')
    assert response.status_code == 200

    hh = HH()
    result = hh.get_vacancies('python', 1)
    assert len(result) == 1
    assert result[0]['id'] == 1
