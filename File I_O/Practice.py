"""
# Homework 1 (Create a file and write text in it)

f = open("Manthan.txt","w")
data = f.write("hi Everyone! \nWe are learning File I/O \nUsing Java \ni Love programming in Java")
f.close()

"""

"""
#Homework 2 (Replace all java with Python)
with open("Manthan.txt" , "r") as f:
    data = f.read()

new_data = data.replace("Java" , "Python")
print(new_data)
# But this will not make changes in the old file so to do that ....

with open("Manthan.txt", "w") as f:
    data = f.write(new_data)
# This will overwrite the original one 

"""
#Homework 3(Check wheather our file contain the word 'learning' or not)
"""

word = "learning"
with open("Manthan.txt" , "r") as f:
    data = f.read()

    if (data.find(word) != -1):
        print("Found")
    else :
        print("not Found")
            
"""
# Homework 4 (WAF to find in while line of the file does the word "learning occur first")  
''' 

word = "learning"
with open("Manthan.txt", "r") as f:
    data = f.readline()
    if (data.find(word) != -1):
        print("Found")
    else:
        print("No found")

    data = f.readline()
    if (data.find(word) != -1):
        print("Found")
    else:
        print("No found")

    data = f.readline()
    if (data.find(word) != -1):
        print("Found")
    else:
        print("No found")    

    data = f.readline()
    if (data.find(word) != -1):
        print("Found")
    else:
        print("No found")   '''

#This is not a very right way so.... see the right one now

"""

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("Manthan.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no +=1

    return -1 

print(check_for_line())    

"""

#Homework 5 (IN a file u were a given numbers seprated by commas and we have to print how many of them are even)
count =0
with open("practice.txt" , "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if (int(val) % 2 == 0):
            count += 1
print(count)            