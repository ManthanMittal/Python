#Sets are collection of unordered items. 
#Each element in a set must be unique and Immutable or we can only store things which are immutable like (string ,tuples ,etc.) we cannot store mutable items like (list and dictionary)

#BUT BUT BUT BUT BUT Sets are Mutable
'''
collection = {1 ,2 ,2 ,2 ,"Hllo" ,"World"}

print(collection)
print(len(collection)) #ans.4 bcoz set ignore duplicate items and store them once

# How to write Empty Set ?
coll = {} #--> Empty dictionary
coll1 = set() #--> Empty Set

print(type(coll))
print(type(coll1))

#Set Methods
coll1.add(5)  #Adds the particular value
coll1.add(1)
coll1.add("Hello")
coll1.add("Hi")

print(coll1)
coll1.remove("Hi") #removes the particular value
print(coll1)

coll1.clear()  #Clears the set
print(coll1)
 

coll2 = {"Hello" , "HI" , "My" , "Name"}

coll2.pop() #Removes a random value everytime we run our code
print(coll2)

'''   
set1 = {1 ,2 ,3 ,4}
set2 = {3 ,4 ,5 ,6 ,7}

print(set1.union(set2)) #Returns a new set and combines values of both sets and ignore duplicate one's
print(set1.intersection(set2)) #Returns the common value from both set and removes the unique one's
print(set1)
print(set2) 

# Homework 1 (Storing 9 and 9.0 as diffrent values in Set)
values = {
    ("float" , 9.0),
    ("int" , 9)
}

print(values)

# or another way
value = {9.0 , "9"}
print(value)