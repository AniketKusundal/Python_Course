# Q.1 Write a python program to perform all set operations. 


set1 = {1 , 6 , 8 , 9 , 7}
set2 = {1 , 2 , 3 , 4 , 5}
print("Orignal Set" , set1)

print("Now Performing the all the Oprations on the set")
print(set1)


#  Opration 1
# print(set1.remove(7))
# print(set1)


# Opration 2

print(set1.pop())
print(set1)


# opration 3
print(set1.issubset(set2))


# Opration 4
print(set1.union(set2))

# Opration 5
print(set1.intersection(set2))


# opration 6
print(set1.difference(set2))