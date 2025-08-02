'''

info = {
    "Name" : "Manthan",
    "Age" : 19,
    "Subjects" : ['Python' ,'HTML' ,'CSS'],  # Lists
    "topics" : ('dict' , 'Sets'),  # Tuple
    "is_adult" : True,  # Boolean
    12.99 : 99.89
}

print(type(info))   #Dictionaries are unordered (No Indexing), Mutable & don't allow duplicate keys
print(info)  

# To access any key's value from a dictoanry we can do it by :
print(info["Name"] , info["Subjects"] )

#To Mutate :
info["Name"] = "MJ"
info["Surname"]  = "Mittal"
print(info)

'''
'''
# Nested Dictionary

student = {
    "Name" : "Manthan",
    "Subjects" : {
        "phy" : 98,
        "chem" : 97,
        "math" : 90

    }
}

print(student["Subjects"]["phy"])  #this prints the mars of "phy"


# Dictionary Methods
# 1. myDict.keys()  #Return all keys
print(student.keys())
#To print in form of list
print(list(student.keys()))
  

# 2. mydict.values()  #Return all Values
print(student.values())

# 3. mydict.items()  #Returns all the key-value pairs as tuples
print(student.items())
print(list(student.items()))
# Now we can apply indexing here after converting it into a list
pair1 = list(student.items())
print(pair1[0])

# 4. mydict.get("Name")  #Returns value of the key
print(student.get("Name"))

# i will think that we can also use print(student["Name"]) which is totally correct bcoz both will return the same value but the main differernce is if we made Name-> Name2 (which doesn't exists in the dictionary) ----- >> in case of get it will return [None] and let the code run further but in case of { print(student["Name"]) } it will return error and don't let our code run further .

# 5. myDict.update(new_Dict)  #Inserts the specified items into Dictionary  
new_Dict = {"name" : "Prisha" , "age" : 12} # if we create same key here , it will overwrite     the                                           original key 
student.update(new_Dict)
print(student)

'''

# Homework 1
marks = {}  #Empty Dictionary

x = int(input("Enter phy :" ))
marks.update({"Phy" : x} )

y = int(input("Enter chem :"))
marks.update({"Chem" : y})

z = int(input("Enter maths :"))
marks.update({"Maths" : z})

print(marks)    