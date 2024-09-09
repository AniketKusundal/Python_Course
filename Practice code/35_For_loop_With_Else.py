'''
----->> The else clause is used along wwith the if statment , Python allows the if Keyword to be usedd with the for and while loop too

---> The else block appers after the body of the loop

---> the statment in the else block while excuted after all itration are completed 

--> The program exist the loop only after the else block is Excted.

'''



# Syntax
# for i in []:
#     print(i)

# else:
#     print("Sorry i is Not Present")



for x in range(5):
    print(f"Itration No {x} in for loop".format(x+1))

else:
    print("Else Block in loop") 
    print("Out of Loop")
