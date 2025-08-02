# Functions in Python
# Block of statement that performs a specific task and we use them to reduce the redundancy(repeativeness) in our code

'''
Format of Function

def func_name(param1 , param2) :     #Function Definition
    #some work
    return val


func_name(arg1 , arg2)      #Function Call

'''

# def cal_sum(a,b):   #Function Definition
#     sum=a+b
#     print(sum)
    

# cal_sum(5 ,100)
# cal_sum(56 , 78)

#What is the use of return the value into a function  
'''
Use return when:

You need the output of a function to use it elsewhere (store, compare, modify).

You're writing modular, testable, and reusable code.

Skip return when:

You're only performing actions like printing, logging, or saving files and don’t need to capture any result. 

'''
'''
# Homework 1
# Average of three numbers
def avg_three(a ,b ,c):
    avg=(a+b+c)/3
    print("Your Average is :",avg)
    return avg

sum = avg_three(1 ,12 ,15)
print(sum)

'''

# Wanna write two print statement but output in same line :
# print("apna college", end=" ") #sep = ""
# print("Python") #end = "\n"

#Functions are of two types:
#1. Built-in functions (print() , len() , type() , range() )
#2. User Defined Function

#Default parameters
def cal_func(a=1 ,b =2):
    sum = a+b
    print(sum)
    return sum

cal_func() # it will work

def cal_pro(a,b=3):   # Default should come in the last 
    pro= a*b
    print(pro)
    return pro

cal_pro(1)    