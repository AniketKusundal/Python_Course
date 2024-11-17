# Q.2 Write a program which accepts 6 integer values and prints “DUPLICATES” if any
# of the values entered are duplicates otherwise it prints “ALL UNIQUE”.
# Example: Let 6 integers are (32, 10, 45, 90, 45, 6) then output “DUPLICATES” to be printed. 


values = list(map(int , input("Enter 6 Integers  :")))

# check if the number of integer is exactly 6

if (values) != 6:
    print("Please enter exactly 6 integers")
else:
    if len(values) != len(set(values)):
        print("DUPLICATES")
    else:
        print("All UNIQUE")