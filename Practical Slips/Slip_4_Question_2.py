# 2 Write a lambda expression to replace characters of given string by other character





import string

replace_char = lambda text , old_char , new_char:  text.replace(old_char , new_char)



input_string = "Hello World"
old_char = "o"
new_char = "1"

print(replace_char(input_string , old_char , new_char))
