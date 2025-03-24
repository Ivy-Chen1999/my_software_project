import unittest
from paymentcard import PaymentCard

class TestPaymentCard(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_constructor_sets_balance_correctly(self):
    # initialize a payment card with 10 euros (1000 cents)
        card = PaymentCard(1000)
        response = str(card)

        self.assertEqual(response, "The card has 10.00 euros")

    def test_eat_affordably_reduces_balance_correctly(self):
        card = PaymentCard(1000)
        card.eat_affordably()

        self.assertEqual(str(card), "The card has 7.50 euros")

    def test_eat_affordably_reduces_balance_correctly_2(self):
        card = PaymentCard(1000)
        card.eat_affordably()

        self.assertEqual(card.balance_in_euros(), 7.5)

    def test_eat_deliciously_reduces_balance_correctly(self):
        card = PaymentCard(350)  
        card.eat_deliciously()

        self.assertEqual(card.balance_in_euros(), 3.50)

    def test_loading_negative_amount(self):
        card = PaymentCard(600)  
        card.load_money(-500)

        self.assertEqual(card.balance_in_euros(), 6.00)

    def test_affordable_lunch_succeeds(self):
        card = PaymentCard(250)  
        card.eat_affordably()

        self.assertEqual(card.balance_in_euros(), 0.00)

    def test_delicious_lunch_succeeds(self):
        card = PaymentCard(400)  
        card.eat_deliciously()

        self.assertEqual(card.balance_in_euros(), 0.00)