import unittest
from scripts.cesar import cifrado


class TestCesar(unittest.TestCase):
    def test_cifra_cadena_vacia(self):
        self.assertEqual(cifrado("c", "", 3), "")

    def test_descifra_cadena_vacia(self):
        self.assertEqual(cifrado("d", "", 3), "")

    def test_cifra_large_text(self):
        self.assertEqual(
            cifrado("c", "El ataque sera a las 10:45", 13), 
            "Ry n6n37r 5r4n n yn5 %${()")

    def test_decifra_large_text(self):
        self.assertEqual(
            cifrado("d", "Ry n6n37r 5r4n n yn5 %${()", 13), 
            "El ataque sera a las 10:45")

    def test_cifra_only_blank(self):
        self.assertEquals(cifrado("c", "  ", 3), "  ")

    def test_descifra_only_blank(self):
        self.assertEquals(cifrado("d", "  ", 3), "  ")

    def test_cifra_zero_key(self):
        self.assertEqual(
            cifrado("c", "El ataque sera a las 10:45", 0), 
            "El ataque sera a las 10:45")

    def test_descifra_zero_key(self):
        self.assertEqual(
            cifrado("d", "El ataque sera a las 10:45", 0), 
            "El ataque sera a las 10:45")