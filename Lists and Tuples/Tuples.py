# Tuples are immuable sequences
tuple = (1 ,2 ,3 ,4)
print(type(tuple))
print(tuple[0]) # Yes Indexing Works here
print(tuple[1])
# tuple[0] = 5  #No bcoz tuples are immutable

#for single element in tuple
#Wrong Form
tup = (1)
print(tup) # 1
print(type(tup))  #integer  #Bcoz a value can be written in just paranthesis , as we write (a+b)

#Right Form
tup =(1,)
print(tup)  #(1,)
print(type(tup))  #tuple

print(tuple[1:4]) #Yes Slicing Works in tuples


#Tuple Methods
hello = (1 ,2 ,3 ,2 ,6 ,7 ,2)
             # Element
               #  |
print(hello.index(1)) #Returns index of first occurence , hello.index(1) is 0
print(hello.count(2)) #counts total occurence , hello.count(2) is 3

