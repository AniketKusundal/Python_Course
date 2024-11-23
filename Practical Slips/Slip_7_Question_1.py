# Q.1 Write a Python program to sum all the items in a dictionary. [10M]
# Sample Dictionary: my_dict = {'data1':100,'data2':20,'data3':50}
# Expected Result: 170 


my_dict = {'sr.No 1': 200 , 'sr.No 2':500 , 'sr.No 3': 1000 , 'sr.No 4':10}

print(my_dict.values())
# Output: dict_values([200, 500, 1000, 10])


# additon of my_dict 
print(sum(my_dict.values()))