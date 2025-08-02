student = ["Manthan" , 95.89 , 17 , "Mittal"]
student[0] = "Mandy"
print(student[0])  # Lists are Mutable unlke Strings
print(student)
print(student[1:4]) # Slicing
print(student[-4:-1]) #negative Slicing

#-------------------------------------------------------------------------------------------------

#List Methods
list = [1 , 2 , 3 , 8 , 56]
print(list.append(5)) # Returns None but for sure adds the element(5) at the end.
list.append(5) # adds one element at the end [1 , 2 , 3 , 8 , 565491 , 5]
print(list)

list.sort() # Sorts in the ascending order and can also be applied on Strings as well in order of their alphabetical order ,but if       (string + integer) is present inside list it will not sort it out 
print(list) 
list.sort(reverse=True) # Sorts in Descending Order
print(list)

list.reverse() #Reverses the list
print(list)

# list.insert(index ,element) #inserts the provided element at provided index
list.insert(1 , 89)
print(list)

list.remove(1) #remove the first occurrence of element
print(list)

#list.pop(index)
list.pop(0) #Removes element at particular index
print(list)

#-------------------------------------------------------------------------------------------------

# Homework 1 (Print name of three movies in a list)
Movie1 = input("Enter your 1st Favourite Movie :" )
Movie2 = input("Enter your 2nd Favourite Movie :" )
Movie3 = input("Enter your 3rd Favourite Movie :" )

List = [Movie1 , Movie2 , Movie3]
print(List)

#-------------------------------------------------------------------------------------------------

# Homework 2 (Elements in list are in Palindrome Order)
el1 = input("Enter your 1st Element :")
el2 = input("Enter your 2nd Element :")
el3 = input("Enter your 3rd Element :")
el4 = input("Enter your 4th Element :")
el5 = input("Enter your 5th Element :")

list1 = [el1 ,el2 ,el3 ,el4 ,el5]
list2 = [el1 ,el2 ,el3 ,el4 ,el5]
list2.reverse()

print(list1)
print(list2)

if(list1 == list2) :
    print("Given Elements in the list are in palindrome.")
else :
    print("Not in Palindrome Order")    