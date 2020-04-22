import unittest
from scripts.detectarEspanol import leer_diccionario, limpiar_texto, es_espanol


class TestDetectarEspanol(unittest.TestCase):
    def test_leer_diccionario(self):
        self.assertEqual(len(leer_diccionario()), 82462)

    def test_blank_limpiar_texto(self):
        self.assertEqual(limpiar_texto(""), "")

    def test_same_limpiar_texto(self):
        self.assertEqual(limpiar_texto("mundo"), "mundo")

    def test_short_limpiar_texto(self):
        self.assertEqual(limpiar_texto("hola mundo"), "holamundo")

    def test_punctuation_limpiar_texto(self):
        self.assertEqual(limpiar_texto("¡hola mundo!"), "holamundo!")

    def test_text1_es_espanol(self):
        res, coef = es_espanol("El diccionario de texto debe tener en \
            letras mayusculas una palabra por linea")
        self.assertEqual((res, round(coef, 2)), (True, 0.92))

    def test_text2_es_espanol(self):
        res, coef = es_espanol(
            "cancionedificioekrkkfnrkjjlsklkdslklwjmsansdoidflkoiwe")
        self.assertEqual((res, round(coef, 2)), (False, 0.28))

    def test_text3_es_espanol(self):
        res, coef = es_espanol("cancionedificio")
        self.assertEqual((res, round(coef, 2)), (True, 1.0))
