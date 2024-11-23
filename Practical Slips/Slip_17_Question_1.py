# .1 Write an anonymous function to display the cube of all elements in the list. 


number = [ 2 , 3 , 4 , 5 , 6]

cube = list(map(lambda x:x**3 , number))

print("Cube of all the numbers in the list" , cube)