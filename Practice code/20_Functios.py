# ---> function is a block of code that perfrom a specific task whenever is called in bif=gger program

# SYNTAX

# def function_name(parameter):
#     # remaning code and statment



def CalculateGmean (a , b):   # here we pass to two arguments 
    mean = (a*b)/(a + b)
    print(mean)


CalculateGmean(30 ,55)    # This is called the function call 



def isGrater(c , d):
    if(c > d):
        print( c ,"First Number is grater")
    else:
        print( d ,"Second number is grater")


isGrater(55 , 100)  # ---> this is function call





def name (fname , lname):
    print("Hello ", fname , lname)
name("Aniket" , "Kusundal")