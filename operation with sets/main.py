#Write a program to create a set and perform the following operations on that set- 1. Create a set with integer elements 2. Create a set with mixed data type elements 3. Create another set with elements - 1, 2, 3, 4, 3, 2 4. Create a set from a list with elements - [1, 2, 3, 2] 5. Print the set after removing the first element from this set - [0, 1, 3, 4, 5]
my_set={1,2,3,4,5}
print("the set is ",my_set)
my_set1={"riddhonil",11,('football','drawing','cricket','coding')}
print("the mix data set is ",my_set1)
my_set2={1,2,3,4,3,2,4}
print("the set removes duplicate ",my_set2)
my_set3=([0, 1, 3, 4, 5])
print("the set 3 is ",my_set3)
my_set3.pop()
print("the set 3 is ",my_set3)
#Write a program to find the intersection of two sets. Set1 = {green, blue} Set2 = {blue, yellow}
set1= {"green","blue"}
set2={"blue","yellow"}
print("the intersection of the two sets is ",set1.intersection(set2))
print("the union of the two sets is ",set1.union(set2))
