# prices of the meals are in cents
AFFORDABLE = 250
DELICIOUS = 400

class PaymentCard:
    def __init__(self, balance):
        # balance is in cents
        self.balance = balance

    def eat_affordably(self):
        if self.balance >= AFFORDABLE:
            self.balance -= AFFORDABLE

    def eat_deliciously(self):
        if self.balance >= DELICIOUS:
            self.balance -= DELICIOUS

    def load_money(self, amount):
        if amount < 0:
            return

        self.balance += amount

        if self.balance > 15000:
            self.balance = 15000

    def __str__(self):
        balance_in_euros = round(self.balance / 100, 2)

        return "The card has {:0.2f} euros".format(balance_in_euros)
    
    def balance_in_euros(self):
        return self.balance / 100