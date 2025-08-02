# range()
# Range function returns a sequence of numbers , starting from 0(by default) , and increment by 1(by default) and stops before a specifid number

#range(start? , stop , step?)     # ? means (optional)
'''
seq = range(5)

for i in seq:
    print(i) #( 0 \n 1 \n 2 \n 3 \n 4)   '''

'''
#Or simply we can write 
for m in range(10):
    print(m)              '''

#Different ways of using range function
'''

for i in range(10):            #range(stop)
     print(i)

for i in range(2, 10):         #range(start ,stop)
     print(i)

for i in range (2 ,10 ,2):     #range(start ,stop ,step)
     print(i)

'''  

'''

#Print number from 100 to 1
for i in range(100 ,0 ,-1):
    print(i)
    
'''

#Print Multiplication table of no. 'N'
n = int(input("Enetr any number :"))
for i in range(1 ,11):
    print(i*n)    