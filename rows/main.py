#Write a program to demonstrate a Floyd triangle pattern?

rows=int(input("how many rows do you want"))
number=1
for i in range(1,rows+1):
    for j in range(i):
        print(number,end=" ")
        number=number+1
    print()
