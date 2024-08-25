#  ---> tuples are immutable hence if you want to add remove or change tuple
#   ---->  items then firstv you must convert the tuple to a list then perfrom opration on that list and convert it back to tuple


countries = ("spain" , "india" , "japan" , "indonashia" , "germany" , "shriLanka")
print(countries)

temp = list(countries)       # convert to list
temp.append("russia")       # add item 
temp.pop(3)                 # remove item
temp[2] = "irland"          # change item
countries = tuple(temp)     # convert it back to the tuple
print(countries)            # print it back countries




# conctination of the tuples

countries1 = ("dubai" , "bharat" , "france" , "paries" , "loandon")

combine = countries + countries1 
print(combine)


