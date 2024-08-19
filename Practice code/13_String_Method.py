# #  string Methods In the python

# # str = "The Loin King , and Loin and tiger is King also "


# # # [1] len()
# # print(len(str))

# # # [2] upper()
# # print(str.upper())


# # # [3] lower()
# # print(str.lower())

# # # [4] strip()    --> removes the white space 
# # print(str.strip())



# # # [5] rstrip()  --> rstrip remove the any tralling chareter example

# # str2 = "aniket is collage student!!!!!"
# # print(str2.rstrip("!"))



# # [5] replace()
# print(str.replace("Loin" , "tiger"))


# # [6] split()
# print(str2.split(" ")) # split the string with white space


# # [7] capitalize()
# print(str.capitalize())


# # [8] center()
# print(len(str.center(50)))

# # [9] count()
# print(str.count("i"))


# # [10] endwith()
# print(str.endswith("g"))


# # [11] find()
# print(str.find("King"))


# # [12] index()  --> the index method search for the first occurance of the given value and return the index where it is present
# print(str.index("Loin"))
# # print(str.index("Loins")) # it gives the error 



# # [13] isalnum() --> it returns true if the  entire string only consistent of A-z a-z 0-9 if aany other charter of punjuation it gives false
# str3 = "WelcomeHoemGT"
# print(str3.isalnum())




# # [14] isalpha()  --> same as the isalnum()
# print(str3.isalpha())



# [14] isprintable()  --> the printable method returns true if all the value whithin the given string are printaable if not then retrun false

str4 = "The Loin King , and Loin and tiger is King also\n "   # it gies the false 
print(str4.isprintable())



# str4 = "The Loin King , and Loin and tiger is King also "   # it gies the false 
# print(str4.isprintable())  --> it gives the true