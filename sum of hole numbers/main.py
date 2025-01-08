#Write a program to calculate the sum of whole numbers.

num=int(input("ENTER A NUMBER"))
sum=0
for i in range(1,num+1):
    sum=sum+i
print("the sum of whole numbers is ",sum)