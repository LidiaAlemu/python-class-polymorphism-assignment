class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")
