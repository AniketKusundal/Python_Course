# Q. 1 Write a recursive function to calculate the sum of numbers from 0 to n. 


def sum_to_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_to_n(n-1)
    
# Taking the input from the user

n = int(input("Enter Non Negative Number :"))

if n < 0:
    print("Please enter a Non Negative integer.")
else:
   # Call the recursive function and display the result
    print(f"The sum of numbers from 0 to {n} is: {sum_to_n(n)}")