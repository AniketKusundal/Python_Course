# Q.1  Write a Python program to find the Factorial of a Number. 



def factorial_nummber(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_nummber(n - 1)
    


num = int(input("Enter The Number To find The Factorial :"))
print(f"The factorial of {num} is {factorial_nummber(num)}")
