# Practice question of function

'''

#Homework 1 (WAP to print the length of a list using a function)
cities = ["Delhi" , "Mumbai" , "Pune " , "Hyderabad"]
heroes = ["Ironman", "Batman" , "Wonder Woman"]
def func_len(list):
    print(len(list))
    return len(list)

func_len(cities)
'''

'''

#Homework 2 (WAF to print the elements of a list ina single line)
def print_list(list):
    for el in list:
        print(el, end=" "   )
    
print_list(heroes)  

'''

'''

#Homework 3 (WAF to find factorial of number n)
def cal_fact(n):
    fact = 1
    for i in range(1 , n+1):
        fact*=i
        i+=1

    print(fact)
    return fact    

m = int(input("Enter any number :"))
cal_fact(m)

'''

"""

#Homework 4
def usd_inr(usd):
    inr_value = usd*83
    print(usd,"USD : ",inr_value,"INR")
    return inr_value

h = int(input("What is your Networth in USD :"))
usd_inr(h)

"""


#Homework 5
#(Write a program which enters a number and check wheather it ia odd oe even and gives bak a string named ODD or EVEN )

def Even_check(n):
    if (n%2 == 0):
        print("EVEN")
    elif(n%2 != 0):
        print("ODD")    

i = int(input("Enter any number :"))
Even_check(i)