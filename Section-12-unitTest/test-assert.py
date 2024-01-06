from unittest import TestCase
from pruebaTestModule import sumar


class TestPrueba(TestCase):
    def test_equal(self):
        self.assertEqual("hola", "hola")
        self.assertNotEqual("hola", "hol")

        assert "hola" == "hola"
        assert "hola" != "hol"

    def test_bool(self):
        self.assertTrue("hola")
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertFalse([])

    def test_is(self):
        self.assertIs("hola", "hola")
        self.assertIsNot("hola", "hol")

    def test_in(self):
        self.assertIn("a", ["a", "b"])

    def test_instance(self):
        self.assertIsInstance("hola", str)
        self.assertNotIsInstance("hola", int)

    def test_raises_without_args(self):
        with self.assertRaises(TypeError):
            sumar()

    def test_raises_with_args_error(self):
        with self.assertRaises(TypeError):
            sumar("", "")