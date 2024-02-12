import requests
import unittest
from unittest.mock import patch
from src.Services.ApiService import ApiService

class TestApiService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_url = 'https://jsonplaceholder.typicode.com/todos/'

    def setUp(self):
        self.api_service = ApiService(self.api_url)

    def test_get_todos_success(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = [{'id': 1, 'title': 'Sample Todo'}]

            todos = self.api_service.get_todos()

            self.assertIsNotNone(todos)
            self.assertEqual(todos, [{'id': 1, 'title': 'Sample Todo'}])

    def test_get_todos_failure(self):
        with patch('requests.get') as mock_get:
            mock_get.side_effect = requests.exceptions.RequestException('Fake error')

            todos = self.api_service.get_todos()

            self.assertIsNone(todos)

if __name__ == '__main__':
    unittest.main()
