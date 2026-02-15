# Week 11: Object-Oriented Programming - Inheritance
# Run: python3 week11-oop/02_inheritance.py

# Inheritance allows a class to inherit attributes and methods from another class
# Parent class (also called base class or superclass)
class Animal:
    """Base class for all animals"""
    
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species
        self.is_alive = True
    
    def eat(self) -> None:
        print(f"{self.name} is eating")
    
    def sleep(self) -> None:
        print(f"{self.name} is sleeping")
    
    def get_info(self) -> str:
        return f"{self.name} is a {self.species}"


# Child class (also called derived class or subclass)
class Dog(Animal):
    """Dog inherits from Animal"""
    
    def __init__(self, name: str, breed: str):
        # Call parent class constructor
        super().__init__(name, "Dog")
        self.breed = breed
    
    # Dog-specific method
    def bark(self) -> None:
        print(f"{self.name} says: Woof!")
    
    # Override parent method
    def get_info(self) -> str:
        return f"{self.name} is a {self.breed} dog"


class Cat(Animal):
    """Cat inherits from Animal"""
    
    def __init__(self, name: str, color: str):
        super().__init__(name, "Cat")
        self.color = color
    
    def meow(self) -> None:
        print(f"{self.name} says: Meow!")
    
    def get_info(self) -> str:
        return f"{self.name} is a {self.color} cat"


# Using inherited classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

# Methods from parent class
dog.eat()
dog.sleep()
print(dog.get_info())

# Dog-specific method
dog.bark()

print()

# Cat methods
cat.eat()
cat.sleep()
print(cat.get_info())
cat.meow()


# More complex inheritance example
class Vehicle:
    """Base class for vehicles"""
    
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False
    
    def start(self) -> None:
        self.is_running = True
        print(f"{self.brand} {self.model} started")
    
    def stop(self) -> None:
        self.is_running = False
        print(f"{self.brand} {self.model} stopped")


class ElectricCar(Vehicle):
    """Electric car with battery"""
    
    def __init__(self, brand: str, model: str, year: int, battery_capacity: int):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity
        self.battery_level = 100
    
    def charge(self) -> None:
        self.battery_level = 100
        print(f"Battery fully charged to {self.battery_level}%")
    
    def drive(self, distance: int) -> None:
        battery_used = distance * 0.2  # 0.2% per km
        if self.battery_level >= battery_used:
            self.battery_level -= battery_used
            print(f"Drove {distance}km. Battery: {self.battery_level:.1f}%")
        else:
            print("Not enough battery!")


class GasCar(Vehicle):
    """Gas car with fuel tank"""
    
    def __init__(self, brand: str, model: str, year: int, tank_size: int):
        super().__init__(brand, model, year)
        self.tank_size = tank_size
        self.fuel_level = tank_size
    
    def refuel(self) -> None:
        self.fuel_level = self.tank_size
        print(f"Tank refilled to {self.fuel_level} liters")
    
    def drive(self, distance: int) -> None:
        fuel_used = distance * 0.1  # 0.1L per km
        if self.fuel_level >= fuel_used:
            self.fuel_level -= fuel_used
            print(f"Drove {distance}km. Fuel: {self.fuel_level:.1f}L")
        else:
            print("Not enough fuel!")


# Using vehicle classes
print("\n--- Electric Car ---")
tesla = ElectricCar("Tesla", "Model 3", 2023, 75)
tesla.start()
tesla.drive(100)
tesla.drive(300)
tesla.charge()
tesla.drive(100)
tesla.stop()

print("\n--- Gas Car ---")
toyota = GasCar("Toyota", "Camry", 2022, 50)
toyota.start()
toyota.drive(100)
toyota.refuel()
toyota.stop()


# TODO: Create a Shape base class with area() method
# TODO: Create Rectangle and Circle classes that inherit from Shape
# TODO: Create an Employee base class with name and salary
# TODO: Create Manager and Developer classes that inherit from Employee
# TODO: Add specific methods to each subclass
