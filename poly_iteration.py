class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def move(self):
        print(f"The {self.year} {self.make} {self.model} is moving.")

class House:
    def __init__(self, address, num_rooms):
        self.address = address
        self.num_rooms = num_rooms

    def move(self):
        print(f"House located at {self.address} with {self.num_rooms} rooms.")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def move(self):
        print(f"{self.name} is {self.age} years old.")

class Plane:
    def __init__(self, airline, model, capacity):
        self.airline = airline
        self.model = model
        self.capacity = capacity

    def move(self):
        print(f"The {self.airline} {self.model} with a capacity of {self.capacity} is flying.")

Car1 = Car("Toyota", "Camry", 2020)
Car2 = Car("Honda", "Civic", 2019)
House1 = House("123 Main St", 3)
House2 = House("456 Elm St", 4)
Person1 = Person("Alice", 30)
Person2 = Person("Bob", 25)
Plane1 = Plane("Delta", "Boeing 737", 180)
Plane2 = Plane("KQ", "Airbus A320", 150)

for obj in [Car1, Car2, House1, House2, Person1, Person2, Plane1, Plane2]:
    obj.move()  # Calls the move method for each object

