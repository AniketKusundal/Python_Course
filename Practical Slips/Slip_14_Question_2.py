# Q. 2 Write a Python program to check whether a given element is present in the given 
# tuple. Display the appropriate message.



countries = ("spain" , "india" , "japan" , "indonashia" , "germany" , "shriLanka")
print("Countries avilable for Travel")



country = input("Enter a country name: ")
if country in countries:
    print(country , "is present in the tuple")
else:
    print(country , "is not present in the tuple")