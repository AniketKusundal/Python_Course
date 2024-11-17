# Q.1 Write an anonymous function to display the cube of all elements in the list


numbers = [ 4 , 5 , 2 , 7]

cube = list(map(lambda x: x**3 , numbers))

print("Cube Of all elements" , cube)
