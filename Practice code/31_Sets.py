# sets is a collection of well defined objects

s = { 1, 5 , 8 , 9 , 7 , 10, 7}
print(s)
print(type(s))


#  set does not contain duplicate values 

# --->> sets are unorderd collecction of data items they store multiple items in single varibables
# --->> sets item are seprated by comma and enclosed with the curly brackets {}
# ---> sets is unchangable meaning you can not changeitem of the sets onece created



info = {"aniket" , 21 , 6.4 , True , 1 , 10 , 2003}
print(info)  #  --> here we see that the item of set occuer in random order and hence they can not be accessed using index number


for value in info:
    print(value)


# Quick Quiz: Try to create an empty set. Check using the type() function whether the type of your variable is a set


quiz = set()
print(quiz)
print(type(quiz))