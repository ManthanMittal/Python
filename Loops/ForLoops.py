# Loops are used for sequential traversal . for traversing list , tuples , strings etc.
#For Loop
'''
nums = [1 ,2 ,3 ,4 ,5]  # same will be for tuples

for vals in nums :
    print(vals)       '''

#We need else when we want to run the loop to the very end but i we don't want to we can simply write in the end print("End")
'''
str = "Manthan Mittal"

for char in str :
    if (char == 'a') :
        print("'a' Found")
        break
    print(char)
else:
    print("End")   '''


#Homework 1

'''
nums = (1 ,4 ,9 ,16 ,25 ,36 ,49 ,64 ,81 ,100)
x = 36
for el in nums:
    if(el == x):
        print("No. found",el)
        break
    print(el)
else:
    print("Finding...")       

'''
# PASS
# pass is null statement that does nothing .It is used as a placeholder for future code

# for el in range(5):
#     #empty           #Error this cant be kept empty 

# print("Hello")   

for el in range(5):
    pass
print("Hello")