"""
# To overwrite the complete data and deleting the previous one
f = open("demo.txt", "w")
f.write("Hello Mittal Sahab")
f.close()

"""

"""

# To add at the end of any data without deleting the previous one
f = open("demo.txt","a")
f.write("\nAree aap hi tou Devta hain")
f.close()

"""

# Now i cannot manually go and create a file so now i will do it in code
# f = open("sample.txt", "w")

# f.close()

# f = open("Hello.txt", "a")
# f.close()

"""
Difference between modes a, a+, w, w+, and r+ in built-in open function : (Stack Overflow)
# Must Search

The argument mode points to a string beginning with one of the following
 sequences (Additional characters may follow these sequences.):

 ``r''   Open text file for reading.  The stream is positioned at the
         beginning of the file.

 ``r+''  Open for reading and writing.  The stream is positioned at the
         beginning of the file.

 ``w''   Truncate file to zero length or create text file for writing.
         The stream is positioned at the beginning of the file.

 ``w+''  Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated.  The stream is positioned at
         the beginning of the file.

 ``a''   Open for writing.  The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar.

 ``a+''  Open for reading and writing.  The file is created if it does not
         exist.  The stream is positioned at the end of the file.  Subse-
         quent writes to the file will always end up at the then current
         end of file, irrespective of any intervening fseek(3) or similar.

"""

# lets give you an example of a+
f = open("demo.txt", "a+")
print(f.read())  # It will read nothing because in append pointer starts from the end
f.write("\nabc")  #but here it will write
f.close()