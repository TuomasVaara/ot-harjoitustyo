import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.maksu = 500
        self.kortti = Maksukortti(500)

    def test_raha_maara_oikea(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_lounas_maara_oikea(self):
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)
    # Maksu käteiselle testit

    def test_kateisosto_edullinen_raha(self):
        self.kassa.syo_edullisesti_kateisella(self.maksu)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)

    def test_kateisosto_maukas_raha(self):
        self.kassa.syo_maukkaasti_kateisella(self.maksu)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)

    def test_kateisosto_edullinen_vaihtoraha(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(self.maksu),260)

    def test_kateisosto_maukas_vaihtoraha(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(self.maksu), 100)

    def test_kateisosto_edullinen_lounas(self):
        self.kassa.syo_edullisesti_kateisella(self.maksu)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_kasteisosto_maukas_lounas(self):
        self.kassa.syo_maukkaasti_kateisella(self.maksu)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_maksu_ei_riita_raha_ei_muutu(self):
        self.maksu = self.maksu -300
        self.kassa.syo_maukkaasti_kateisella(self.maksu)
        self.assertTupleEqual((self.kassa.kassassa_rahaa, self.kassa.syo_maukkaasti_kateisella(self.maksu), self.kassa.maukkaat), (100000, 200, 0))

# Maksu kortilla testit

    def test_korttimaksu_edullinen_kortin_saldo(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), True)
        self.assertEqual(str(self.kortti), "saldo: 2.6")

    def test_korttimaksu_edullinen_lounas_maara(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_korttimaksu_maukas_kortti_saldo(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), True)
        self.assertEqual(str(self.kortti), "saldo: 1.0")

    def test_korttimaksu_maukas_lounas_maara(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_korttimaksu__ei_tarpeeksi_rahaa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), False)
        self.assertEqual(str(self.kortti), "saldo: 1.0")

    def test_korttimaksu_ei_tarpeeksi_rahaa_lounas(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_korttimaksu_ei_tarpeeksi_rahaa_maukkaat_saldo(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), False)
        self.assertEqual(str(self.kortti), "saldo: 1.0")

    def test_korttimaksu_ei_tarpeeksi_rahaa_maukkaat_saldo(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_kassan_raha_ei_muutu_korttimaksussa_edullinen(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kassan_raha_ei_muutu_korttimaksusta_maukas(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kassan_raha_ei_muutu_kun_korttimaksu_ei_onnistu(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_rahaa_ladattaessa_kortin_ja_kassan_rahat_kasvavat_oikein(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100500)
        self.assertEqual(str(self.kortti), "saldo: 10.0")

    def test_ei_voi_ladata_negatiivista_rahaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(str(self.kortti), "saldo: 5.0")


    def test_maksu_ei_riita_lounas_ei_muutu(self):
        self.maksu = self.maksu - 300
        self.kassa.syo_edullisesti_kateisella(self.maksu)
        self.assertTupleEqual((self.kassa.kassassa_rahaa, self.kassa.syo_maukkaasti_kateisella(self.maksu), self.kassa.maukkaat), (100000, 200, 0))
