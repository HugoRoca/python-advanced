from unittest import TestCase
from pruebaTestModule import sumar


class TestPrueba(TestCase):
    def test_suma_sin_argumentos(self):
        with self.assertRaises(TypeError):
            sumar()

    def test_suma_argumentos_erroneos(self):
        with self.assertRaises(TypeError):
            sumar(None, None)
            sumar(1, "1")
            sumar([], {})

    def test_suma(self):
        valor_esperado = 4
        resp = sumar(2, 2)
        self.assertEqual(resp, valor_esperado)