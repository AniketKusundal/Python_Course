# Q.2 Write a Python class that has two methods: 
# get_String and print_String, get_String
# accept a string from the user and print_String prints the string in upper case. 



class StringClass:
    def __init__(self):
        self.str = ""


    def get_String(self):
        self.str = input("Enter a string: ")
    
    def print_String(self):
       print("Getting the string and converting to the upper case :" , self.str.upper())


# creating the objecct of the string class
StringClass_Editor = StringClass()


StringClass_Editor.get_String()

StringClass_Editor.print_String()






