# Q. 1 Write a program which finds sum of digits of a number. [10M] 
# Example n=130 then output is 4 (1+3+0).


def sum_of_digits(n):
    total = 0

    while n > 0:
        total += n % 10   # Get the last digit 
        n = n / 10 # Remove the last digit

    return total

# getting input from the user 

num = int(input("Enter the Number for the sum : "))


#  calculate and display the sum of digit

result = sum_of_digits(num)
print("Sum of digits of the number is: ", result)  # Output: Sum of digits
