class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}")

class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, strap_color):
        super().__init__(brand, model, price)
        self.strap_color = strap_color

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}, Strap: {self.strap_color}")
