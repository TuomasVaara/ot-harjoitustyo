import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate(100000)
        self.lounaat = 0

    def test_raha_maara_oikea(self):
        self.assertEqual(self.kassapaate, 100000)
        
    def test_lounas_maara_oikea(self):
        self.assertEqual(self.lounaat, 0)

    def test_kateisosto_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        
    def test_kateisosto_maukas(self):
