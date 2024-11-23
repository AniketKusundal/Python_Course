# Q.1 Write a Python Program to Find the Factorial of a Number


num1 = int(input("Enter The Number Do You want to find the factorial Of : "))

if num1 < 0:
    print("Sorry, factorial does not exist for negative numbers")
else:

    fact = 1
    for i in range (1 , num1 , +1):
        fact = fact * 1
        print("The factorial of", num1, "is", fact)