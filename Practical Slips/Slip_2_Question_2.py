# Q.2 Write a Python program to print list after removing ODD numbers


odd = [ 4 , 1 , 2 , 3 , 8 , 99 , 7]

print("Origrnal List Is" , odd)


odd_Numbers = [num for num in odd if num % 2 != 0 ]

print("After removing the odd numbers from the list: ", odd_Numbers)