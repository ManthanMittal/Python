val1 = input("Enter your Value :", )
print (type(val1) , val1)
# But this will always give type as string bcoz of the default setting of Input Function

# so to input integer or float value we have to use type casting
val2 = int(input("Enter your Value :" ))
print (type(val2) , val2)