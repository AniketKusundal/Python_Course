# [1] Update ()  ->> this  method update the values of the key provided to it if  the item already exist in the dictionary , else it create a new key value - pairs

ep1 = {122 : 54 , 155 : 70 , 778 : 90 , 126 : 90} 
ep2 = {301 : 88 , 302 : 95}


# ep1.update(ep2)
# print(ep1)



#  Removing items from the dictonary :   ----> there are few items taht we can use to remove item from dictonary 

# [2]  clear()    -- Removes all the elements from the dictionary

# ep2.clear()
# print(ep2)   # O/P  -- {}


#  how to create empty dictonary 

# empt = {}
# print(empt)



# [3] pop() --->   Removes the element with the specified key values pairs  whose key passed as a parameter 

# ep1.pop(122)
# print(ep1)



#  [4]  this method removes the last key value pairs from the dictonary 


# ep1.popitem()
# print(ep1)




# [5] del() ----> delete keyword removes the dicctonary item

# del ep2
# print(ep2)



# NOTE   if key is not provided then del keyword will delete the dictonary entierly

del ep1(155)
print(ep1)