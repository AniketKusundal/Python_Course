import time

Current_Hour = int(time.strftime('%H'))
print(Current_Hour)



if Current_Hour < 12:
    print("Goood Morning Sir")

elif(Current_Hour < 18):
    print("Good Afternoon Sir")
else:
    print("Good Eving Sir ")