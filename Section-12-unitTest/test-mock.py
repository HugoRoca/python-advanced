from unittest import TestCase
from unittest.mock import patch

from pruebaTestModule import Calc, exec_magic


class TestPrueba(TestCase):

    @patch("pruebaTestModule.magic")
    def test_mock_error(self, mock):
        mock.side_effect = Exception

        with self.assertRaises(Exception):
            exec_magic()

    @patch("pruebaTestModule.magic")
    def test_magic(self, mock):
        print("START MOCK")
        mock.return_value = "Hola"
        response = exec_magic()
        print(response)
        print("END MOCK")

    @patch.object(Calc, "suma")
    def test_mock(self, mock):
        mock.return_value = 10
        calc = Calc.suma(5, 20)

        print(calc) # == 10


"""
    def test_magic2(self):
        print("START WITHOUT MOCK")
        response = exec_magic()
        print(response)
        print("END WITHOUT MOCK")
"""