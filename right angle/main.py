#Write a program to demonstrate a right angle triangle pattern?

rows=int(input("how many rows do you want"))

for i in range(1,rows+1):
    print()
    for j in range(i):
        print("*",end="")