import unittest
from scripts.atbash import cifrado


class TestAtbash(unittest.TestCase):
    def test_cadena_vacia(self):
        self.assertEqual(cifrado(""), "")

    def test_only_symbol(self):
        self.assertEqual(cifrado("@#$"), "")

    def test_only_lower_text(self):
        self.assertEquals(cifrado("mundo"), "NFMWL")

    def test_only_lower_text_reverse(self):
        self.assertEquals(cifrado("NFMWL"), "MUNDO")
    
    def test_only_upper_text(self):
        self.assertEquals(cifrado("MUNDO"), "NFMWL")
    
    def test_lower_and_upper_text(self):
        self.assertEquals(cifrado("MunDO"), "NFMWL")
    
    def test_numeric(self):
        self.assertEquals(cifrado("3421"), "")

    def test_numeric_and_text(self):
        self.assertEquals(cifrado("m3u4n7do"), "NFMWL")

    def test_large_text(self):
        self.assertEquals(cifrado("La mision ha sido un exito"), "OZ NRHRLM SZ HRWL FM VCRGL")
    
    def test_large_text_reverse(self):
        self.assertEquals(cifrado("OZ NRHRLM SZ HRWL FM VCRGL"), "LA MISION HA SIDO UN EXITO")

    def test_only_blank(self):
        self.assertEquals(cifrado("  "), "  ")
