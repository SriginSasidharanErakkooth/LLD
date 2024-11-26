# Target interface
class PaymentProcessor:
    def process_payment(self, amount):
        pass

# Adaptee classes
class GooglePay:
    def make_payment(self, amount):
        print(f"Google Pay: Payment of {amount} processed successfully.")

class Paytm:
    def initiate_payment(self, amount):
        print(f"Paytm: Payment of {amount} initiated.")

    def confirm_payment(self, amount):
        print(f"Paytm: Payment of {amount} confirmed successfully.")

class PhonePe:
    def send_money(self, amount):
        print(f"PhonePe: Money transfer of {amount} completed.")

# Adapter classes
class GooglePayAdapter(PaymentProcessor):
    def __init__(self):
        self.google_pay = GooglePay()

    def process_payment(self, amount):
        self.google_pay.make_payment(amount)

class PaytmAdapter(PaymentProcessor):
    def __init__(self):
        self.paytm = Paytm()
        

    def process_payment(self, amount):
        self.paytm.initiate_payment(amount)
        self.paytm.confirm_payment(amount)

class PhonePeAdapter(PaymentProcessor):
    def __init__(self):
        self.phone_pe = PhonePe()

    def process_payment(self, amount):
        self.phone_pe.send_money(amount)

# Client code
def main():
    payment_processor = PaytmAdapter()

    amount = 1000
    payment_processor.process_payment(amount)
    

if __name__ == "__main__":
    main()