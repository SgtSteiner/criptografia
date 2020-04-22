import unittest
from scripts.cesarHack import hack_cesar, ALFABETO


class TestCesarHack(unittest.TestCase):
    def test_todas_claves(self):
        results = hack_cesar("241on0q1 yn s7r4#n o476n")
        self.assertEqual(len(results), len(ALFABETO))

    def test_una_clave(self):
        results = hack_cesar("241on0q1 yn s7r4#n o476n")
        self.assertEqual(results[13], "probando la fuerza bruta")

    def test_zero_clave(self):
        results = hack_cesar("probando la fuerza bruta")
        self.assertEqual(results[0], "probando la fuerza bruta")
