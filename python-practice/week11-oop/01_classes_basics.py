# Week 11: Object-Oriented Programming - Classes Basics
# Run: python3 week11-oop/01_classes_basics.py

# What is OOP?
# Object-Oriented Programming organizes code around "objects" that have:
# - Attributes (data/properties)
# - Methods (functions/behaviors)

# Creating a simple class
class Dog:
    """A simple class representing a dog"""
    
    # Constructor - runs when creating a new object
    def __init__(self, name: str, age: int):
        self.name = name  # Attribute
        self.age = age    # Attribute
    
    # Method - a function that belongs to the class
    def bark(self) -> None:
        print(f"{self.name} says: Woof!")
    
    def get_info(self) -> str:
        return f"{self.name} is {self.age} years old"


# Creating objects (instances of the class)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Using object methods
dog1.bark()
dog2.bark()

# Accessing attributes
print(f"\nDog 1: {dog1.name}, Age: {dog1.age}")
print(f"Dog 2: {dog2.name}, Age: {dog2.age}")

# Using methods that return values
print(f"\n{dog1.get_info()}")
print(f"{dog2.get_info()}")


# More complex example - Person class
class Person:
    """Represents a person with name, age, and hobbies"""
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.hobbies = []  # Empty list to store hobbies
    
    def add_hobby(self, hobby: str) -> None:
        self.hobbies.append(hobby)
        print(f"Added {hobby} to {self.name}'s hobbies")
    
    def introduce(self) -> None:
        print(f"\nHi! I'm {self.name}, {self.age} years old.")
        if self.hobbies:
            print(f"My hobbies are: {', '.join(self.hobbies)}")
        else:
            print("I don't have any hobbies yet.")
    
    def have_birthday(self) -> None:
        self.age += 1
        print(f"Happy birthday {self.name}! You are now {self.age}!")


# Using the Person class
person1 = Person("Alice", 25)
person1.add_hobby("Reading")
person1.add_hobby("Coding")
person1.introduce()
person1.have_birthday()


# Class with class variables (shared by all instances)
class Car:
    """Represents a car"""
    
    # Class variable - shared by all Car objects
    wheels = 4
    
    def __init__(self, brand: str, model: str, year: int):
        # Instance variables - unique to each object
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
    
    def drive(self, miles: int) -> None:
        self.mileage += miles
        print(f"Drove {miles} miles. Total mileage: {self.mileage}")
    
    def get_description(self) -> str:
        return f"{self.year} {self.brand} {self.model}"


car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2021)

print(f"\n{car1.get_description()}")
print(f"Wheels: {car1.wheels}")  # Class variable

car1.drive(100)
car1.drive(50)

print(f"\n{car2.get_description()}")
car2.drive(200)


# TODO: Create a Book class with title, author, and pages attributes
# TODO: Add a method to the Book class that returns a description
# TODO: Create a Student class with name, grade, and a list of courses
# TODO: Add methods to add courses and display student info
