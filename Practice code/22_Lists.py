#  list are the orderd collection of data items 
#  they store multiple values in single varibable


marks = [4 , 5, 7 , 10  , 22 , 11]

print(marks)
# print(type(marks))
# print(marks[0])


# print("Negative Indexing")
# print(marks[-6]) --> negative index
# print(marks[len(marks)-2])  --> postive index

# print(marks[6-1])  postive index


# if 8 in marks:
#     print("Yes")
# else:
#     print("No")


#  same thing apply for the string
# if "ani" in "aniket":
#     print("yoo")
# else:
#     print("Noo")






print("multiple values in single variable")
marks2 = [4 , 5, 7 , 10  , 22 , 11 , "Aniket" , True]
print(marks2)   # O/P   [4, 5, 7, 10, 22, 11, 'Aniket', True]
print(marks2[:])  # O/P   [4, 5, 7, 10, 22, 11, 'Aniket', True]
print(marks2[1:2])   #O/P   [5]
print(marks2[1:8:2]) # Jumping index    O/P  [5, 10, 11, True]
