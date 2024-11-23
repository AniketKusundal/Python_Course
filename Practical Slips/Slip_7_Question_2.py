# Q. 2. Write a Python function that takes a number as a parameter and display factorial
# of it. 


def function(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * function(num - 1)
    
print(function(5))
