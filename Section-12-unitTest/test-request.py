from unittest import TestCase
from unittest.mock import patch
import json

from pruebaTestModule import get_games


class TestPrueba(TestCase):

    @patch("requests.get")
    def test_mock(self, mock):
        with open("data.txt", "r", encoding="utf-8") as file:
            expected_response = json.loads(file.read())

        mock.return_value.status_code = 200
        mock.return_value.json.return_value = expected_response

        response = get_games()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response)