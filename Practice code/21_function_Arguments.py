# There are Four types of arguments that we can provide in a function

    # [1]   Defult Arguments
    # [2]   Keyword Arguments 
    # [3]   Variable Length Argument
    # [4]   Rquire Arguments


# def average (a , b):
#     print("The Average Is : " , (a +b)/2)

# average(5 , 6)




# [1]   Defult Arguments    ---> we can provide a defualt value while creating function

def average (a=9 , b = 6):
    print("Ther Average is " , (a + b)/2)

average(1 , 2)    # this is calledd defulat function argument


# [EXAMPLE 2] :

# def name (fname , mname = "jhon" , lname = "whatsaon"):
#     print("Hello" , fname ,mname,lname)

# name("Aniii")




# [2]   Keyword Arguments --->> We can provide the argument with key=value this way the interpreter recognize the argument by the parameter name.

# hence the order is in which the argument are passed does not matter 


# def fullName(fname , Mname , Lname):
#     print("Hello" , fname , Mname , Lname)

# fullName(Mname="jhon" , Lname="walker" , fname="JD")



# [3]   Variable Length Argument    ---> In case we do not pass th arguments with key =value syntax Then it is nesscary to pass the arguments in the correct Position order and the number passed show match with actuall function defination 


# [Example - 1] :

# def name (fname , mname , lname):
#     print("Hello" , fname , mname , lname)

# name("peter" , "dany" , "quill")



def avg (a , b , c = 1):
    print("The Avarage is " , (a + b + c)/2)

avg(5 , 6)




# [3]   Variable Length Argument  ---> Sommetimes we mayv need to pass more arguments than those defined in the actual function
        #  This can be done using variable length arguments 



# Abirty Arguments  -->>  While creating a function pass a  before the parameter name while defining the function

# the function access the arguments by processing then in the of tuple



def Average(*number):
    print(type(number))
    sum = 0
    for i in number:
        sum = sum + i
        print("Average is : " , sum/len(number))

Average(2,5,6,4,1)





#  RETURN STATMENT --->> The return statment is used to return the value of the expression back to the calling function


def name(fname , mname , lname):
    return "Hello , " + fname + " " + mname + " " + lname
print(name("ani" , "ket" , "Mumbai"))