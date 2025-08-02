# Methods 
# Methods are function that belongs to objects.

"""

class Student:
    college_name = "ABC College"

    def __init__(self , name ,marks):
        self.name = name
        self.marks = marks

    def welcome(self):  # Function inside class are methods
        print("Welcome Student" , self.name)

    def get_marks(self): # Function inside class are methods
        return self.marks  

s1 = Student("Karan" ,97) 
s1.welcome()
print(s1.get_marks())

"""

"""

#Practice Question 1
class Student:

    def __init__(self , name ,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val

        print("hi" , self.name , "your average score is :" ,sum /3)   

s1 = Student("tony stark", [99 ,98 ,97])  
s1.get_avg()           

s1.name = "ironman" #We can also change them
s1.get_avg()

"""

"""

# Static Methods
# Methods that don't use the self parameter (works at a class level)

class Student:
    @staticmethod  #decorator
    def college ():
        print("ABC College")

# Decorator allow us to wrap another functionin order to extend the behavior of wrapped function , without permanently modifying it .

"""

#Practice Question 2
class Account:
    def __init__(self ,bal ,acc):
        self.balance = bal
        self.account_no = acc

    #debit method
    def debit(self ,amount):
        self.balance -= amount
        print("Rs.",amount ,"was Debited")
        print("total balance =", self.get_balance())

    #credit method
    def credit(self ,amount):
        self.balance += amount
        print("Rs.",amount ,"was Credited")    
        print("total balance =", self.get_balance())

    def get_balance(self):
        return self.balance    


acc1 = Account(100000 , 12345)
acc1.debit(50000)  
acc1.credit(500000)