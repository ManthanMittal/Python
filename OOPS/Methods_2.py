
# Super Method
# super() method is used to accessmethods of parent class

class Car:
    color = "black"

    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car Started...")

    @staticmethod
    def stop():
        print("Car stopped...")

class ToyotaCar(Car):
    def __init__(self , name , type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar("supra" , "Petrol")
print(car1.type) 


#class method
# a class method is bound to the class recieves the class as an implicit first argument .

# note :static methods can't access or modifyclass state & generally for utility

"""

class Person:
    name = "anonymous"

    # def changeName(self , name):
    #     self.__class__.name = "Manthan"

    @classmethod
    def changeName(cls ,name):
        cls.name = name

p1 = Person()  
p1.changeName("Manthan Mittal")
print(p1.name)
print(Person.name)  

"""
# Property Method
class Student:
    def __init__(self , phy , chem ,maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.maths) / 3) + "%"    
    
stud1 = Student (98 ,97 ,99)
print(stud1.percentage)    

stud1.phy = 86
print(stud1.percentage)


# Homework
# 1.Getter
# 2.Setter

# Polymorphism : Operator Overloading
# When the same operator is allowed to have different meanings according to the context
# Operators and Dunders Functions 

# Lets create a code for the calculation of complex numbers
"""
class Complex:
    def __init__(self ,real ,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +", self.img,"j")  

    def add(self ,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img    
        return Complex(newReal ,newImg) 

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4 ,6)
num2.showNumber()

num3 = num1.add(num2) #NO Error
num3.showNumber

num3 = num1 +num2 # Error
num3.showNumber() (Bcoz hmne complex number ke liye addintion ko define hi nhi kiya h )

"""
# but Using Dunder function

"""
class Complex:
    def __init__(self ,real ,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +", self.img,"j")  

    def __add__(self ,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img    
        return Complex(newReal ,newImg) 

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4 ,6)
num2.showNumber()

# num3 = num1.add(num2) #NO Error
# num3.showNumber

num3 = num1 +num2 #No Error
num3.showNumber()

"""

"""
 For subtraction (__sub__)
 For multiplication (__mul__)
 For division (__truediv__)
 For modulo (__mod__)
 
 """

# Homework 1
'''
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius **2 
    
    def Perimeter(self):
        return 2 *3.14 *self.radius
    
c1 = Circle(7)
print(c1.area())
print(c1.Perimeter())

'''

# Homework 2
'''

class Employee:
    def __init__(self ,role ,dept ,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role) 
        print("dept =", self.dept)   
        print("salary =", self.salary)

class Engineer(Employee):
        def __init__(self ,name ,age):
            self.name = name
            self.age = age
            super().__init__("Engineer", "IT" , "75,000")   

e1 = Engineer("Elon Musk" ,40)
e1.showDetails() 

'''
#Homework 3
class Order:
    def __init__(self ,item ,price):
        self.item = item
        self.price = price

    def __gt__(self ,odr2):
        return self.price > odr2.price

odr1 = Order("chips", 20)
odr2 = Order("tea", 15)    

print(odr1 >odr2) #True                                                                                                                                                                                                                                                            
