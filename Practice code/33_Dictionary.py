
''' 
    --->  it is a combinnation of key value pairs 
    ---> dictionnary is a order collection of data 
    -->     They store multiple values is in single variable They are enclosed with {} curly brakets and seprated by the comma 
'''


info = {"name" :"aniket" , "Age" : 21 , "eligible" : True }
print(type(info))



dic = {

    344 : "aniket",
    555 : "shubh" ,
    445 : "nanu" , 
    748 :  "bob" ,
    111 : "jack",
    111 : "jack"   # duplicate not allowed 
}

print(dic)
print(len(dic))   #  legth of the dictionary 



# [1]  Accessing Single Value   --> values in dictnory ca be assccing using key 
# print(info["Age"])
# 
# ----> We can access dictionary values by mentioning key  in square brackets , either by using Get method
# print(info.get("eligible"))

# print(info["Age2"])               # --> it prints KeyError when key is not present 
 
# print(info.get("eligible2"))   # --> it prints none when key is not present 







#  [2]  Accessing Multiple Values :- ---> we can print the values in the dictonary using value method() 

#print(info.keys())    # O/P   dict_keys(['name', 'Age', 'eligible'])
#print(info.values())  # O/P   dict_values(['aniket', 21, True])


for keys in info.keys():
    print(f"Key is corresponding to the Key {keys} is {info[keys]}")






#  [3] Accessing Key Values - pairs :

print(info.items())   #  O/P    dict_items([('name', 'aniket'), ('Age', 21), ('eligible', True)])

for key,values in info.items():
    print(f"Key is corresponding to the Key  {key}  is {values}")