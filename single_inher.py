class Vehicle:
    def __init__(self, brand, model, name, color, availability):
        self.brand = brand
        self.model = model
        self.name = name
        self.color = color
        self.availability = availability

class Bike(Vehicle):
    def __init__(self, vehicle_type, brand, model, name, color, availability):
        super().__init__(brand, model, name, color, availability)
        self.vehicle_type = vehicle_type

    def display_info(self):
        print("Type of vehicle is:", self.vehicle_type)
        print("Availability:", self.availability)
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Name:", self.name)
        print("Color:", self.color)

obj1 = Bike("Two-wheeler", "Hero", "Pleasure", "XXX", "Blue", "Yes")
obj1.display_info()


