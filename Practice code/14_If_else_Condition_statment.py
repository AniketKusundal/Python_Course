#   If Else Conditional Statment in Python
#  ----> The conditional statment are further classified into following types
# [1]  if
# [2]  if-else
# [3]  if-else-elif
# [4]  nasted if-else-elif




# [2]  if-else
# Example [1]

# a = int(input("Enter Your Age : "))
# print("Your age is : " , a)

# if(a > 18):
#     print("You can Vote")

# else:
#     print("You Can't Vote")



# Example [2]

# applePrice = 210
# budget = 220

# if(applePrice <= budget):
#     print("Alexa ,  Add 1 Kg Apples in Basket")
# else:
#     print("Alexa , Don't Buy apple")







# [3]  if-else-elif

# num  = int(input("Enter The Value of num : "))

# if(num < 0):
#     print("Number Is Negative")

# elif(num == 0):
#     print("Number is zero")

# elif(num == 1000):
#     print("Number Is Spcial For me")

# else:
#     print("Number is Positive")





# [4]  nasted if-else-elif

num = 15

if(num < 0):
    print("Number is Negative")

elif(num > 0):
    if(num <= 10):
        print("Number is b/w 1-10")
    elif(num > 10 and num <= 20):
        print("Number is b/w 10-20")

    else:
        print("Number is Grater than 20 ")

else:
    print("Number is zero")


    
    