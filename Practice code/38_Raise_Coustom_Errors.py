#   In python we can raise the custom error using ([raise]) keyword.



# [EXAMPLE 1]

# a = int(input("Enter a number b/w 5 to 9 : "))

# if(a < 5 or a > 9):
#     raise ValueError("Value should be b/w 5 and 9")


# [EXAMPLE 2]

salary = int(input("Enter Salaray Amount : "))
if not 2000 < salary < 5000:
    raise ValueError ("Not a Valid Salary")


#   --> we learned about diffrent built in rexception in python and why it is importatnt to handel exception
#   ---> some times we may need to create our own coustom exceptions taht serve our purpose 



#  QUIZ


brocode = input("Enter secrate code :")

if (brocode != 'quiz'):
    raise ValueError("clud code is not match")


