import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    #not good at finnish so I wrote test functions in english

    def test_card_balance_is_correct_at_start(self):
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 10.00 euroa")

    def test_loading_money_increases_balance(self):
        self.maksukortti.lataa_rahaa(300)  
        self.assertEqual(self.maksukortti.saldo_euroina(), 13.00)

    def test_withdrawing_money_decreases_balance_if_enough(self):
        self.maksukortti.ota_rahaa(500)  
        self.assertEqual(self.maksukortti.saldo_euroina(), 5.00)

    def test_withdrawing_money_does_not_change_balance_if_not_enough(self):
        self.maksukortti.ota_rahaa(2000)  
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)

    def test_withdraw_returns_true(self):
        result = self.maksukortti.ota_rahaa(500)  
        self.assertTrue(result)

    def test_withdraw_returns_false(self):
        result = self.maksukortti.ota_rahaa(2000)  
        self.assertFalse(result)


