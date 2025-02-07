#Write a program to generate a random integer and match it with the input given by the user?

import random
num1=random.randint(0,10)
choice=int(input("enter your choice"))
if num1==choice:
    print("your choice matches the computers choice")
else:
    print("your choice doesent matches with the computers choice")