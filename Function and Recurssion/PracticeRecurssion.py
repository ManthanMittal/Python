# Practice ques. of Recurssions

# Question 1
def sum(n):
    if (n == 0):
        return 0
    else :
        return n + sum(n-1)
    
print(sum(10))    


# Question 2
# This is how i tried to approach this problem
"""

Hello = ["Hello" , "World" , "Manthan" , "Mittal" , "HI"]

def print_list(list):
    idx = 0
    if(idx == len(list)):
        return 
    else :
        print(list[idx] )
        idx+=1
        
"""

#Right Answer

Hello = ["Hello" , "World" , "Manthan" , "Mittal" , "HI"]

def print_list(list , idx):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list , idx+1)


print_list(Hello , 0)