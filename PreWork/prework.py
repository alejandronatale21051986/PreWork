class PaymentBroker():
    def __init__(self, name):
        self.name = name

    def pay(self):
        print(f'Pagando con: {self.name}')
            
    


pb = PaymentBroker("MercadoPago")
pb.pay()

pb1 = PaymentBroker("Broker PayPal")
pb1.pay()