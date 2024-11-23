# Q.2 Write a Python program to remove duplicate elements from the list. 





def remove_duplicates(input_list):
    return list(set(input_list))




list1 = ["Banana" , "apple" , "kiwi" , "Banana" , 4 , 5 , 2 , 1] 

unique_list = remove_duplicates(list1)



print("Orignall List" , list1)
print("List after removing duplicates" , unique_list)


