import unittest
from scripts.transColumnHack import criptoanalisis


class TestTransColumnHack(unittest.TestCase):
    def test_full_Descifr(self):
        criptograma = "EABRN NRDUC EANHN RLAOM UDQEG EUACI RUEDY REOOL NAAOC MMO"
        criptograma.replace(" ", "").lower()
        self.assertEqual(
            criptoanalisis(criptograma),
            "14 -> enunlugardelamanchadecuyonombrenoquieroacordarme"
        )
