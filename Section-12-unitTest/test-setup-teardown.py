from unittest import TestCase


class TestPrueba(TestCase):
    def setUp(self) -> None:
        self.frase = "I'm phrase"
        print("Me ejecuto antes de que arranque el test")

    def tearDown(self) -> None:
        print("Ahora me ejecuto yo, soy el teardown")

    def test_prueba(self):
        print(self.frase)

        self.assertEqual(self.frase.lower(), "i'm phrase")
        self.frase = "other"

    def test_prueba2(self):
        print("-" * 300)
        print(self.frase)