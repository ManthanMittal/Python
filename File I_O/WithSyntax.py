with open("demo.txt" , "r") as f:
    data = f.read()
    print(data)

with open("demo.txt" , "w") as f:
    f.write("Haan Vi Kive hon")    
    
#Isme hme file ko close krne ki jrurt nhi hoti , with syntax apne aap manage kr leta h 
