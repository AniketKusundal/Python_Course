# Q. 1 Write a python program to check if a string is a Palindrome or Not. 


def palindrome(s):
    return s == s[::-1]



s = "Aniket Kusundal"
ans = palindrome(s)

if ans:
    print("yes")

else:
    print("No")