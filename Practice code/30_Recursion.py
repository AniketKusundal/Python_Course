#  Resuction In Python   --->>> resuction is the process of defining something in term of itself 

#   --->> a physical word example would be to place two parller mirrors facing each other Any object in b/w them would be refflected recursively



#               Python Recursive Function             #

# --->> we know that function can call ther function it is even possible for the function to call itself

# this type of constraints are termed as a recursive function





# Factorial (n) = n * factorial (n-1)


def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)# -->  here we call the function with diffrent argument
    
print(factorial(5))

# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
#   5 * 4 * 3 * 2 * 1

# QUIZ   


def fibonacci(num):
    if(num == 0):
        return 0
    
    elif (num == 1):
        return 1
    else:
        return fibonacci (num - 1) + fibonacci(num - 2)
    
print(fibonacci(2))

# fibonacci(0) = 0
# fibonacci(1) = 1
# fibonacci(2) = fibonacci(1) + fibonacci(0) = 1 + 0 = 1
# fibonacci(3) = fibonacci(2) + fibonacci(1) = 1 + 1 = 2
# fibonacci(4) = fibonacci(3) + fibonacci(2) = 2 + 1 = 3
# fibonacci(5) = fibonacci(4) + fibonacci(3) = 3 + 2 = 5
