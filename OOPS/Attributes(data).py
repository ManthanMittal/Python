# Class and Instance Attributes(Data)
class Student:
    college_name = "ABC College"
    name = "Anonymous" # Class attribute

    def __init__(self ,name ,marks):
            self.name = name  # Object Attribute
            self.marks = marks
            print("Adding new student in database...")


s1 = Student("Karan",97) 
# Now what will be printed here bcoz class attri. says name = anonymous but obeject attribute says karan 
# Object attribute will be given prefrence
# Obj attri. > Class Attri.

print(s1.name ,s1.marks)  #Karan