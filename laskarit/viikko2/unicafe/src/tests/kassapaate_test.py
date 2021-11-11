import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.maksu = 500
        self.kortti = Maksukortti(1000)
    #ok
    def test_raha_maara_oikea(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    #ok
    def test_lounas_maara_oikea(self):
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)
    # Maksu käteiselle testit
#ok
    def test_kateisosto_edullinen_raha(self):
        self.kassa.syo_edullisesti_kateisella(self.maksu)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
#ok
    def test_kateisosto_maukas_raha(self):
        self.kassa.syo_maukkaasti_kateisella(self.maksu)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
#ok
    def test_kateisosto_edullinen_vaihtoraha(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(self.maksu),260)
#ok
    def test_kateisosto_maukas_vaihtoraha(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(self.maksu), 100)
#ok
    def test_kateisosto_edullinen_lounas(self):
        self.kassa.syo_edullisesti_kateisella(self.maksu)
        self.assertEqual(self.kassa.edulliset, 1)
#ok
    def test_kasteisosto_maukas_lounas(self):
        self.kassa.syo_maukkaasti_kateisella(self.maksu)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_maksu_ei_riita_raha_ei_muutu(self):
        self.maksu = self.maksu -300
        self.kassa.syo_maukkaasti_kateisella(self.maksu)
        self.assertTupleEqual((self.kassa.kassassa_rahaa, self.kassa.syo_maukkaasti_kateisella(self.maksu), self.kassa.maukkaat), (100000, 200, 0))
        return False

