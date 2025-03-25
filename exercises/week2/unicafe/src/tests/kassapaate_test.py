import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    #not good at finnish so I wrote test functions in english
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_cash_register_initial_values(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)  
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_cash_purchase_affordable_lunch_sufficient(self):
        amount = self.kassapaate.syo_edullisesti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)  
        self.assertEqual(self.kassapaate.edulliset, 1)  
        self.assertEqual(amount, 160)

    def test_cash_purchase_affordable_lunch_not_sufficient(self):
        amount = self.kassapaate.syo_edullisesti_kateisella(150)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)  
        self.assertEqual(self.kassapaate.edulliset, 0)  
        self.assertEqual(amount, 150)

    def test_cash_purchase_delicious_lunch_sufficient(self):
        amount = self.kassapaate.syo_maukkaasti_kateisella(600)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)  
        self.assertEqual(self.kassapaate.maukkaat, 1)  
        self.assertEqual(amount, 200) 

    def test_cash_purchase_delicious_lunch_insufficient(self):
        amount = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)  
        self.assertEqual(self.kassapaate.maukkaat, 0) 
        self.assertEqual(amount, 200) 

    def test_card_purchase_affordable_lunch_sufficient(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.kortti)) 
        self.assertEqual(self.kortti.saldo, 760)  
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)  

    def test_card_purchase_delicious_lunch_sufficient(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.kortti))  
        self.assertEqual(self.kortti.saldo, 600) 
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)  

    def test_card_lunch_count_increases_correctly(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)  
        self.assertEqual(self.kassapaate.maukkaat, 1)  

    def test_card_purchase_affordable_lunch_insufficient(self):
        card = Maksukortti(100)  
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(card))  
        self.assertEqual(card.saldo, 100)  
        self.assertEqual(self.kassapaate.edulliset, 0)  
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)  

    def test_card_purchase_delicious_lunch_insufficient(self):
        card = Maksukortti(200)  
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(card))  
        self.assertEqual(card.saldo, 200)  
        self.assertEqual(self.kassapaate.maukkaat, 0)  
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)  

    def test_loading_money_onto_card(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 100) 
        self.assertEqual(self.kortti.saldo, 1100)  
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)  

    
    def test_loading_negative_amount(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -200)  
        self.assertEqual(self.kortti.saldo, 1000)  
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)  

    def test_cash_register_balance_in_euros(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)