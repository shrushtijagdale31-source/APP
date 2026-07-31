# Strategy Classes
class CreditCard:

    def pay(self):
        print("Payment made using Credit Card")


class DebitCard:

    def pay(self):
        print("Payment made using Debit Card")


class UPI:

    def pay(self):
        print("Payment made using UPI")


# Context Class
class Payment:

    def __init__(self, strategy):
        self.strategy = strategy

    def process(self):
        self.strategy.pay()


# Main Program
print("Select Payment Method")
print("1. Credit Card")
print("2. Debit Card")
print("3. UPI")

choice = int(input("Enter your choice: "))

if choice == 1:
    p = Payment(CreditCard())
elif choice == 2:
    p = Payment(DebitCard())
elif choice == 3:
    p = Payment(UPI())
else:
    print("Invalid Choice")
    exit()

p.process()