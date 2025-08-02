# OPP in Python
# to map with real world senarios , we started using objects in code
# This is called object oriented Programming

# Class and Object in python
# class is blueprint for creating objects
"""
class Student:      #class
    name = "Karan"

s1 = Student()      #object
print(s1.name)   

s2 = Student()      #object
print(s2.name)

"""

class Car:
    color = "blue"
    brand = "BMW"

car1 = Car()
print(car1.color)

car2 = Car()
print(car2.brand)

#__init__ Function

# Constructor
# All classes have a function called __init__() ,Which is always executed when the object is being initiated (weather we write it or not) .

#Creating Class

class Student:
    # default constructor
    # def __init__(self):
    #     pass

    #parameterised constructor
    def __init__(self ,name ,marks):
        self.name = name  # both name are diff. one is for assigning values and other one is output.
        self.marks = marks
        print("Adding new student in database...")

#Creating Object
s1 = Student("Karan",97) 
print(s1.name ,s1.marks)        

#The self parameter is a refrence to the current instance of the class , and is used to access variables that belongs to the class

s2 = Student("Arjun",87)
print(s2.name ,s2.marks)

 