#    String Slicing And Opration On the string 


str = "Tiger live in forest"

print(str.__len__())


#  string as an array 

animal =  "Elephent"

animalLen = len(animal)
print(animalLen)

print(animal[1:5])   # include 1 but not 4
print(animal[0:4])   # include 0 but not 4
print(animal[:5])




print(" For Negative Slicing")

print(animal[0 :-3]) 
print(animal[ :len(animal)-4]) 
print(animal[-3 : -1])