# # Q.1 Write a Python program to count the number of occurrences of each 
# character in a string. Sample String: google.com' 
# Expected Result: {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1} 

# Function to count character occurrences
def count_characters(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Sample string
sample_string = "google.com"

# Count character occurrences
result = count_characters(sample_string)

# Display the result
print("Character count:", result)


