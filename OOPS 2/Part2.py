# del Keyword
# used to delete object properties or object itself .
"""
class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Manthan")
print(s1.name) #Manthan
del s1.name
print(s1.name) #Error (object attribute deleted)

"""
# Private (like) Attributes and Methods
# private attributes and methods are meant to be used onl within the class and not accessible  from outside the class
# to make any sttribute private we just place (__)
"""
class Account :
    def __init__(self ,acc_no , acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  #Privatization

acc1 = Account("12345" , "abcde")  

print(acc1.acc_no)
print(acc1.__acc_pass) #Error

"""
# But we can print it in a class


class Account :
    def __init__(self ,acc_no , acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  #Privatization

    def reset_pass(self):
        print(self.__acc_pass)    

acc1 = Account("12345" , "abcde")  

print(acc1.acc_no)
print(acc1.reset_pass()) 

# ANother Brainstorming
class Person:
    __name = "anonymous"

    def __hello(self):
        print("Hello Person!")

    def Welcome(self):
        self.__hello()

p1 = Person()

print(p1.Welcome())

# Summary : agr hmne private kr diya kisi cheej ko then uske sirf class ke internal functions hi access kr skte h