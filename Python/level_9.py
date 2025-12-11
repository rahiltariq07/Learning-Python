# ## OOP Concept.

# # 1. What is OOP?
# # Object-Oriented Programming (OOP) models programs like the real world: you create classes (blueprints) and objects (things made from that blueprint).
# # A class describes what an object has (attributes) and what it can do (methods).
# # Analogy:
# # Class = blueprint for a car.
# # Object = a specific car built from that blueprint (red Honda, 2016).
# # Attributes = color, model, fuel.
# # Methods = drive(), stop(), honk().

# # 2. Basic Anatomy
# class Car:
#     def __init__(self, make, model):
#         self.make = make # attribute
#         self.model = model

#     def drive(self): # method
#         print(f"{self.make} {self.model} is driving")

# # Create objects
# c1 = Car("Honda", "City")
# c1.drive() # Honda City is driving

# # - __init__ is the constructor. Runs when object is created
# # - slef refers to the current object's instance

# # Trial
# class Employee:
#     def __init__(self, id, name, age):
#         self.id = id
#         self.name = name
#         self.age = age
    
#     def work(self):
#         print(f"Employee with Id: {self.id}, Name: {self.name} & Age: {self.age} is working")

# employee1 = Employee(1, "Rahil", 23)
# employee1.work()

# # 3. The 4 Pillars of OOP
# # 3.1 Encapsulation:
# # Hide internal details, expose simple interface.
# # Simple Idea: Keep related data and methods together and hide internals
# # so other code doesn't break things by changing internal directly.

# # Analog: A TV remote, you press buttons; you don't need to know the internal circuits.

# # Python Approach
# # - In Python we conventionally use:
#     # - public attributes: obj.x
#     # - protected (convention): _x (single underscore)
#     # - private (nam-mangled): __x (double underscore -> _ClassName__x)
# # - Prefer properties (getters/setters) to safely expose data.

# # eg: 
# class BankAccount:
#     def __init__(self, owner, balance = 0):
#         self.owner = owner
#         self.__balance = balance #private
    
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             return amount
#         raise ValueError("Insufficient funds")
    
#     def get_balance(self):
#         return self.__balance

# acc1 = BankAccount("Rahil", 100)
# acc1.deposit(50)
# acc1.withdraw(10)
# print(acc1.get_balance())
# print(acc1.owner)

# # 3.2 Abstraction
# # Show only what is necessary
# # Simple Idea: hide complexity and show a simple interface.

# # Analogy: You drive a car, you use the steering wheel and pedals, you don't neeed the engine schematics.

# # e.g: (abstract base class)
# # Python provides ***abc*** module to enfore an interface:

# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, r):
#         self.r = r
    
#     def area(self):
#         import math
#         return math.pi * self.r * self.r
    
# c = Circle(5)
# print(c.area())

# # Shape defines the abstract contract: any subclass must implement area().

# # In Python, abstract base classes (ABCs) and interfaces use the same syntax, because Python has no separate interface keyword.

# # Both are written like this:
# # from abc import ABC, abstractmethod
# class Example(ABC):
#     @abstractmethod
#     def method(self):
#         pass

# # Whether this becomes:
# # an abstract class, or
# # an interface
# # depends entirely on how you use it.

# # 3.3 Inheritance
# # Reuse and extend behavior
# # Simple idea: a class (child) can inherit attributes/methods from another (parent).

# # Analogy: Vehicle -> Car -> Electric Car.
# # Car inherits form Vehicle and adds specifics.
# # e.g:
# class Vehicle:
#     def start(self):
#         print("Starting engine")

# class Car(Vehicle):
#     def honk(self):
#         print("Beep!")

# my_car = Car()
# my_car.start()
# my_car.honk()

# # Use ***super()*** to call parent constructor or methods:
# class ElectricCar(Car):
#     def __init__(self, make, battery_size):
#         super().__init__()  # call parent init if needed
#         self.make = make
#         self.battery = battery_size

# # Multiple inheritance
# # Python allows multiple inheritance (***class A(B, C): ***).
# # Python uses MRO (method resolution order) and super() follows MRO. ****Need to Check****.

# # 3.4 Polymorphism
# # same interface, different behaviors
# # Simple idea: different objects respond to the same method call in their own way.

# # Analogy: ***play()***, a musician plays piano vs a guitarist plays guitar, same action name but different behavior.

# # e.g:
# class Animal:
#     def speak(self):
#         print("...")

# class Dog(Animal):
#     def speak(self):
#         print("Woof!")

# class Cat(Animal):
#     def speak(self):
#         print("Meow!")

# animals = [Dog(), Cat()]

# for a in animals:
#     a.speak() # calls Dog.speak then Cat.speak

# # Operator overloading (another polymorphism)
# # using magic methods like ***__add__***, ***__len__***:

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
    
#     def __repr__(self):
#         return f"Point({self.x}, {self.y})"

# p1 = Point(1, 2)
# p2 = Point(3, 4)

# print(p1 + p2) # Point(4, 6)

# # 4. Other essential OOP topics in Python
# # 4.1 Class vs Instance variables
# # - Instance variable: **self.x**, unique per object.
# # - Class variable: **ClassName.x**, shared across all instances.

# class Dog:
#     species = "Canis lupus" # class variable

#     def __init__(self, name):
#         self.name = name # instance variable

# # 4.2 ***@classmethod and @staticmethod***
# # - @classmethod recieves class **cls** - good for alternative constructors
# # - @staticmethod has no **self** or **cls** - utility function placed inside class.

# class Person:
#     population = 0

#     def __init__(self, name):
#         self.name = name
#         Person.population += 1

#     @classmethod
#     def from_fullname(cls, fullname):
#         first = fullname.split()[0]
#         return cls(first)
    
#     @staticmethod
#     def is_adult(age):
#         return age >= 18

# # 5. Best practices & tips (short)
# # - Keep classes focussed (single responsibility)
# # - Use composition over deep inheritance where possible
# # - Use encapsulation to protect invariants (private vars + properties)
# # - Prefer clear method names
# # - Use ***super()*** for cooperative multiple inheritance
# # - Write small classes for tests

# # 6. Full Example tying pillars together

# from abc import ABC, abstractmethod

# class Employee(ABC):
#     def __init__(self, name, salary):
#         self._name = name # Protected
#         self.__salary = salary # Private

#     @property
#     def name(self):
#         return self._name
    
#     @property
#     def salary(self):
#         return self.__salary
    
#     @abstractmethod
#     def calculate_bonus(self):
#         pass

# class Developer(Employee):
#     def calculate_bonus(self): # Polymorphism
#         return self.salary * 0.10
    
# class Manager(Employee):
#     def calculate_bonus(self):
#         return self.salary * 0.20
    
# # using them
# people = [Developer("Rahil", 100000), Manager("Ali", 120000)]

# for p in people: # polymorphic call
#     print(p.name, p.calculate_bonus()) # Rahil 10000.0; Ali 24000.0


# # Practice Questions
# # Q.no.: 1
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
    
#     def describe(self):
#         print(f"{self.title} by {self.author}")

# book1 = Book("A God doesn't Plead", "Rahil Tariq")
# book1.describe()

# # Q.no.: 2
# class Vehicle:
#     def move(self):
#         print("Vehicle is moving")
    
# class Car(Vehicle):
#     def move(self):
#         print("Car is driving")

# class Bike(Vehicle):
#     def move(self):
#         print("Bike is pedaling")

# vehicles = [Car(), Bike()]

# for v in vehicles:
#     v.move()

# # Q.no.: 3
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, base_salary=0):
        # assign to internal variable (not the @property) to avoid setter error
        self._name = name
        self.__salary = base_salary   # private

    @property
    def name(self):
        # read-only property for name
        return self._name

    @property
    def salary(self):
        # read-only salary property
        return self.__salary

    @abstractmethod
    def calculate_pay(self):
        pass

    def __str__(self):
        return f"{self.name}: Pay = {self.calculate_pay():.2f}"


class FullTimeEmployee(Employee):
    def __init__(self, name, base_salary):
        # call parent ctor which sets _name and __salary
        super().__init__(name, base_salary)

    def calculate_pay(self):
        # 10% bonus
        bonus = self.salary * 0.10
        return self.salary + bonus

    def __str__(self):
        return f"FullTime - {self.name}: Base = {self.salary:.2f}, Total Pay = {self.calculate_pay():.2f}"


class PartTimeEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        # pass 0 as base_salary; part-timers compute from hours * rate
        super().__init__(name, base_salary=0)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_pay(self):
        return self.hours_worked * self.hourly_rate

    def __str__(self):
        return (f"PartTime - {self.name}: Hours = {self.hours_worked}, "
                f"Rate = {self.hourly_rate:.2f}, Pay = {self.calculate_pay():.2f}")


# --- Example usage ---
if __name__ == "__main__":
    ft = FullTimeEmployee("Rahil", 100000)
    pt = PartTimeEmployee("Aman", hours_worked=80, hourly_rate=250)

    employees = [ft, pt]

    for e in employees:
        print(e)
        print("Calculated pay:", e.calculate_pay())
        print("---")


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Corolla")
print(my_car.brand)