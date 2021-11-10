import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    def test_kortin_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    def test_rahan_lataus_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti),"saldo: 1.1")
    def test_saldo_vähenee_oikein_jos_kortilla_on_tarpeeksi_saldoa(self):
        self.maksukortti.lataa_rahaa(490)
        self.maksukortti.ota_rahaa(400)
        self.assertEqual(str(self.maksukortti),"saldo: 1.0")
    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti),"saldo: 0.1")
    def test_riittaako_raha(self):
        alkup = self.maksukortti
        self.maksukortti.ota_rahaa(10)
        if self.assertEqual(self.maksukortti, alkup):
            return False
        return True
        
