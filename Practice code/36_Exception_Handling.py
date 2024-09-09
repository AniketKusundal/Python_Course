#  Exception handeling is the process of responding to unwanted Or enexpected events when a company program run

#  Exception Handeling deals with these events to avoid the program or system crashing and without this process exceptions would disrupt the normal Opration of a program

# EXCEPTION IN PYTHON
#  Python has many built in exceptions that are eaised when your program encounters an Error Somethings in profgram goes Wrong
# When the exception occur the python Interpreter stop the current proccess and passes it to the calling process . until it is handled. If Not handel Program will crash



# PYTHON try....except

# try except block are used inpython to handel errors and Exception . The code inn try block runs when there is no error when the try block catches the error , When the except block is excted



# EXAMPLE [1]
 
a = input("Enter The Number : ")
print(f"Multipication of tabel {a} is :")
try:
    for i in range(1 ,11):
        print(f"int{a} X {i} = {int(a)*i}") 
except:
    print("Invalid Input")
print("Some Imp Lines of code")
print("End OF Program")

#   NOTE  --> In this code when user Enter String value ir Enter string The error is occour And code goes to  [except block] And user Enter Interger  value multiplication table wil print successfully


# EXAMPLE [2]

try:
    num = int(input("Enter an interger value :"))
except ValueError:
    print("Number Entered Not an Interger")
