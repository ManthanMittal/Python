# There are 4 Important Pillars of OOPS
# 1. Abstraction
# 2. Encapsulation
# 3. Inheritance
# 4. Polymorphism

 
# 1. Abstraction
# Hiding the implementation details of a class and only showing the essential features to a user

# 2. Encapsulation
# Wrapping data and functions into a single unit object

# 3. Inheritance
# when one class (child/derived) derives the properties and methods of another class(parent/base).

"""
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car Started...")

    @staticmethod
    def stop():
        print("Car stopped...")

class ToyotaCar(Car):
    def __init__(self , name):
        self.name = name

car1 = ToyotaCar("Fortuner")               
car2 = ToyotaCar("Supra")

print(car1.start())
print(car1.color)

"""

# Types :
# 1. Single Inheritance
# 2. Multi-level inheritance
# 3. Multiple Inheritance

# Multi level Inheritance

"""
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car Started...")

    @staticmethod
    def stop():
        print("Car stopped...")

class ToyotaCar(Car):
    def __init__(self , brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

car1 = Fortuner("diesel")
car1.start() 
"""      

#Multiple Inheritance
"""
class A:
    varA = "Welcome to Class A"

class B:
    varB = "Welcome to class B"

class C(A ,B):
    varC = "Welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varC)
"""
