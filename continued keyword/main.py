#Write a program to display 1 to 10 numbers in reverse order and skip the number 5.
for i in range(10,1,-1):
    if i==5:
        continue
    else:
        print(i)