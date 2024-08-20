#  devlopers coming from the laguage like c/c++ or java know that there is a coditionnal statment know as switch case
#  ---> this match case is the switch case of pytho which was introduced in python



#       SYNTAX

# simple match case statement
def runMatch():
    num = int(input("Enter a number between 1 and 3: "))
    
    # match case
    match num:
        # pattern 1
        case 1:
            print("One")
        # pattern 2
        case 2:
            print("Two")
        # pattern 3
        case 3:
            print("Three")
        # default pattern
        case _:
            print("Number not between 1 and 3")
            
runMatch()
