'''
i = 1

while (i <= 5) :
    print(i)
    i+=1 

print(i)  '''

'''
m = 100
while(m >= 1) :
    print(m)
    m-=1

print("loop ended")  '''

#Homework 1
# Finding an element in a tuple

'''
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

i = 0
while (i < len(nums)) :
    if (nums[i] == x) :
        print("Number found at index :",i)
    else:
        print("Finding...")   
    i += 1

print("End of the loop")       ''' 

# Same using 'Break' keyword

'''
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

i = 0
while (i < len(nums)) :
    if (nums[i] == x) :
        print("Number found at index :",i)
        break    
    else:
        print("Finding...")   
    i += 1

print("End of the loop")    '''

#Same using the 'continue' keyword , lest suppose we dont dont want to print the no.3

i = 0

while (i<=5) :
    if (i == 3) :
        i += 1
        continue #skip
    print(i)
    i+=1
