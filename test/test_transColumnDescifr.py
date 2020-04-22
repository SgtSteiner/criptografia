import unittest
from scripts.transColumnDescifr import descifrar


class TestTransColumnDescifr(unittest.TestCase):
    def test_blank_Descifr(self):
        self.assertEqual(descifrar("", 10), "")

    def test_full_Descifr(self):
        criptograma = "ELUTL ARAAE ARSST CEERC DIRET E".replace(
            " ", "").lower()
        self.assertEqual(descifrar(criptograma, 8),
                         "elartedelaescriturasecreta")

    def test_fail_Descifr(self):
        criptograma = "ELUTL ARAAE ARSST".replace(" ", "").lower()
        self.assertIsNot(descifrar(criptograma, 8),
                         "elartedelaescriturasecreta")
