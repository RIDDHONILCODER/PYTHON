#Write a program to understand how the value error exception works?
try:
    choice=int(input("enter a number"))
    if choice>=0 and choice<=10:
        print("its a number")
except ValueError as ex:
    print(ex)       