# Q.1 Write a program which prints Fibonacci series up to n terms. 


def fibonacci(n):
    if n <= 0:
        print("Plese Enter The Positive Number")
        return
    
    # Starting Values
    a , b = 0 , 1
    print("Fibonacci Series up to", n, "terms:")
    for i in range(n):
        print(a , end = " ")
        a , b = b , a + b


# taking the user input

n = int(input("Enter The Number : "))
fibonacci(n)