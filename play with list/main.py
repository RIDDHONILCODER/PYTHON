#Write a Python program to find the sum and average of the list. The average of the list is defined as the sum of the elements divided by the number of the elements. Also, find the largest and the smallest number in the list.
list=[1,2,3,4,5,20,60,35,46,72,85,39]
print("the number of elements of the list is ",len(list))
sum=0
for i in list:
    sum=sum+i
print("the sum of the elements are ",sum)
average=sum/len(list)
print("the average of the list is ",average)
list.sort()
print("the new list is ",list)
print("the smolest number is ",list[0])
print("the largest number is ",list[-1])