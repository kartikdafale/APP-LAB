class UPI:
    def pay(self, amount):
        print(f"\nPayment of {amount} made using UPI.\n")

class NetBanking:
    def pay(self, amount):
        print(f"\nPayment of {amount} made using Net Banking.\n")

class CreditCard:
    def pay(self, amount):
        print(f"\nPayment of {amount} made using Credit Card.\n")

class DebitCard:
    def pay(self, amount):
        print(f"\nPayment of {amount} made using Debit Card.\n")

class PaymentProcessor:
    def __init__(self, payment_method):
        self.payment_method = payment_method
        
    def process_payment(self, amount):
        self.payment_method.pay(amount)

print("===== Payment Processing System =====")
print("The Modes of Payment:--")
print("1. UPI")
print("2. Net Banking")
print("3. Credit Card")
print("4. Debit Card")

choice = int(input("Enter your choice: "))
amount = float(input("Enter Amount: "))

if choice == 1:
    payment = UPI()

elif choice == 2:
    payment = NetBanking()

elif choice == 3:
    payment = CreditCard()

elif choice == 4:
    payment = DebitCard()

else:
    print("Invalid Choice")
    exit()

processor = PaymentProcessor(payment)

processor.process_payment(amount)