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


phone1 = Smartphone("Apple", "iPhone 15", 999)
phone1.info()
phone1.call("123-456-7890")

watch1 = Smartwatch("Apple", "Watch Series 9", 499, "Black")
watch1.info()
watch1.call("987-654-3210")

class Vehicle:
    def move(self):
        pass 

class Car(Vehicle):
    def move(self):
        print("Car is driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Plane is flying ✈️")

vehicles = [Car(), Plane()]

for v in vehicles:
    v.move()
