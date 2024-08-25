#  it is a new string formating mechanism introdused by the PEP 496 (Python Enhacement Praposal)
#  it is also known as litral string interpolustionor more commaly as F-String

# ---> when we prefix the string with the letter F the string becomes the f-string itself can be formatted in much same as the str.format method



country = "india"
name = "aniket"

print(f"Hey i'm {name} i'm from {country}")


#  EXAMPLE [2]   

price = 48.099999
txt = f"for only {price: 2f} dollors !..."
print(txt)
print(type ("{2 * 30}"))