# ----> The Break statment enables a program to skip over a aprt of the code
#  -----> the break statment terminates the very loop lies within





# Break Statment
# for i in range(12):
#     if(i == 10):
#         break
#     print("5 X" , i+1 , "=" , 5 * (i+1))
# print("Loop ko Chokdkar nikal gaya")





# With Continue

# for i in range(12):
#     if(i == 10):
#         print("Skip The Intration")
#         continue
#     print("9 X" , i+1 , "=" , 9 * (i+1))



# --> the cotinue statment skips the rest of the next iteration it occurs


# [EXAMPLE 2]

for i in [2 , 5 ,7 , 8 , 22 , 34]:
    if(i%2 !=0):
        continue
    print(i)




#  For Do While Loop In Python 

#  Emulate the do while loop in the python 

i = 0
while True:
    print(i)
    i = i + 1
    if(i % 100 == 0):
        break
    