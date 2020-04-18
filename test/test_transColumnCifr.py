import unittest
from scripts.transColumnCifr import cifrar, salida


class TestTransColumnCifr(unittest.TestCase):
    def test_blank_salida(self):
        self.assertEqual(salida(""), "")

    def test_default_bloque_salida(self):
        self.assertEqual(salida("12345678"), "12345 678")

    def test_define_bloque_salida(self):
        self.assertEqual(salida("ABCDEFGH", 3), "ABC DEF GH")

    def test_long1_cifrar(self):
        mensaje = "el arte de la medicina".replace(" ", "")
        self.assertEqual(cifrar(mensaje, 7), "eeclliaanrmateeddi")

    def test_long2_cifrar(self):
        mensaje = "el arte de la medicina consiste en entretener al \
                  paciente mientras la naturaleza cura la enfermedad".replace(" ", "")
        self.assertEqual(
            cifrar(mensaje, 7),
            "eecsencilarelliineiealaraanstrennelmrmatrantazaeteceeltrtaededoetpeaucnadinneamsrufd"
            )

    def test_completo_cifrar(self):
        mensaje = "el arte de la medicina consiste en entretener al \
                  paciente mientras la naturaleza cura la enfermedad".replace(" ", "")
        self.assertEqual(
            salida(cifrar(mensaje, 7)).upper(),
            "EECSE NCILA RELLI INEIE ALARA ANSTR ENNEL MRMAT RANTA ZAETE CEELT RTAED EDOET PEAUC NADIN NEAMS RUFD"
            )
