#String Functions
str = "i am a Coder am ama ama am ama am am am am"

print(str.endswith("er")) #Returns True if string ends with substr
print(str.capitalize()) #Capilatizes the The first letter of the String but does not changes the original String

#To change the origibal String we can do something like 
str = str.capitalize()
print(str)

print(str.replace("a","o")) #Replacec all occurences of "old" with "new" one
print(str)

print(str.find("coder")) #Returns 1st Index of the 1st Occurer

print(str.count("am ")) #Counts the occurrence of substr


#Homework 1 
m = input("Enter your first name :" )
print(len(m))

#Homework 2
y = "Heloo $ i am $ , your bf $ is your gf $$"
print(y.count("$"))

