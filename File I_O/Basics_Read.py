# File I/O in Python
#Python can be used to perform operations on a file. (read and write data)
#
# Types of files :
#  1. Text Files : .txt , .docs , .log etc.
#  2. Binary Files : .mp4 , .mov , .png , .jpeg etc.

"""

f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

"""

'''
character         Meaning

'r'          :    open for Reading(Default)
'w'          :    open for writing , trancating the file first (Deleting before writing)
'x'          :    create a new file and open it for writing
'a'          :    open for writing, appending to the end of the file if it exists
'b'          :    binary mode
't'          :    text mode (default)
'+'          :    open a disk file for updating (reading and writing)

'''

# if you want to read certain number of characters
f = open("demo.txt")

# data = f.read(5)  # this will read the starting 5 characters
# print(data)    

# data = f.readline()  #reads one line at a time
# print(data)

# this will give a empty line under the written text line bcoz when we hit enter on our keyboard it places a invisible \n at that line which is read by the python file and while executing that file this \n shows a empty line afterwards

# NOTE : Readed line can't be read again ,Take it as a pointer going over over your every text. 'but but but' if we want to solve this always close your file after opening it and then before reopening first open file again

data = f.read()
print(data)  #Executed
f.close()

f = open("demo.txt")
data = f.read()
print(data)  #Can't be executed bcoz a thing once read can't be read again

