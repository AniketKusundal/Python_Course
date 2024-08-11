#  Write A program to find the sum of natural Numbers 


num = int(input("Enter a Number :"))

if num < 0:
    print("Plese Enter a Positive Number :")
    
else:
    sum = 0
    while num > 0:
        sum += num
        num -= 1
        print(sum)