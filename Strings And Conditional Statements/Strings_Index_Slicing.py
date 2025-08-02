a = "Manthan "
b = "Mittal"

print(a+b) #Contatenation

str1 = "This is Manthan"
str2 = 'This is me'
str3 = """Hello thi is me"""

# we have 3 ways to represent a string , we need them bcoz sometime we need to use "" , '' in our string itself

# for single line 
val1 = "This is String . We are creating it in Python."
print(val1)
# for next line in same string
val2 = "This is String. \nWe are Creating it in Python." 
print(val2)
# for tab space in same string
val3 = "This is String. \tWe are Creating it in Python." 
print(val3)

print(len(a))   

#Indexing in String (Starts from zero and goes ON)
n = "Manthan Mittal"
print(n[0])

# We cannot Manipulate Indexing

#Slicing (Accesing Parts of the String)
# str[star_ind : ending_ind] (ending index is not included)

# A p p l e
# 0 1 2 3 4

print(n[0:7])
print(n[:4]) #print(n[0:4])
print(n[4:]) #print(n[4:len(n)])

#Negative Slicing  
# A   p  p  l   e 
# -5 -4 -3 -2  -1

print(n[-5:-1])
