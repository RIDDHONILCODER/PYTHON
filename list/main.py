#Write a program to perform the following operations on a List: 1. Create an empty list 2. A list with elements 3. Use * operator 4. Reverse a list
#creating empty list
list=[]
print("The empty list is {} ".format(list))
#create a list with 5 elements
list=[1,2,3,4,5]
print("the list is {} ".format(list))
#using multiply oprator
list1=list*3
print("the value is {} ".format(list1))
listnew=list1[::-1]
print("the revers list is {} ".format(listnew))