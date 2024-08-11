# Write a Program In Python To find Amstrong  number in an Interval


lower = int(input("Enter Lower Limit Here: "))
upper = int(input("Enter Upper Limit Here: "))

for num in range (lower , upper + 1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
sum += digit ** order
temp //=10 # reduce the number by removing the last digit
if num == sum:
    print(num)
