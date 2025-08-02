# Recurssion is when a function call itself repeatedly
#Recursive Function
"""
def show(n):
    if (n==0):  # Base Case
        return
    print(n)
    show(n-1)  # Here function calls itself again

show(5) 
 """  

#Recurssion work as a stack flow in a memory first it goes from n to 1 then 1 to n again and checking wheather all the orders are executed or not 
"""
def show(n):
    if (n==0):  
        return
    print(n)
    show(n-1)  
    print("END")  # SO "end" will be printed 5 times 

show(5)

"""

#Another Example 
def fact(n):
    if (n ==0 or n ==1):
        return 1
    else:
        return n*fact(n-1)
    
print(fact(5))