'''
age = int(input("What is your age :" ))

if (age >= 18) :
    print("Can Vote and Drive")
elif(age < 18) :
    print("Can't Vote and Drive")     '''

# We can also use if always instead of elif , but the main diffrence btwn them is if we use if (it will check all the statements) and if we use elif (it only checks ince we get a true statement)
'''
marks = 74

if (marks >= 90) :
    Grade = "A"
elif(marks >= 80 and marks < 90) :
    Grade = "B"
elif(marks >= 70 and marks <80) :
    Grade = "C"
else:
    Grade = "D"

print("Grade of the Student is ->",Grade)   ''' 


#NESTING
# Using contidion in condition or use if under if condition

#Homework 1
#(Print the largest of 4 numbers)

a = int(input("Enter 1st Number :" ))
b = int(input("Enter 2nd Number :" ))
c = int(input("Enter 3rd Number :" ))
d = int(input("Enter 4th Number :" ))

if (a>b and a>c and a>d):
    print("Your largest no. is 1st :",a)
elif(b>c and b>d):
    print("The largest number is 2nd :",b)
elif(c>d):
    print("The largest number is 3rd :",c)   
else:
    print("The largest number id 4th :",d)  

print("End of the code")      