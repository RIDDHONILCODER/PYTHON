#Write a program to perform the following operations: 1. Create a tuple with different datatypes 2. Create another tuple of integers 3. Create a new tuple by adding 9 to the previous tuple 4. Count the occurrences of an element in the tuple 5. Perform slicing on the tuple
#1. Create a tuple with different datatypes
tuple1=("riddhoil","football","drawing",25,65,37,"#",24.5,65.4,45.6,True)
print("the tuple is ",len(tuple1))

#3. Create a new tuple by adding 9 to the previous tuple
#Create another tuple of integers
tuple2=(10,45,78567,28,647,56,345,10,10)
tuple2=tuple2+(9,)

#4. Count the occurrences of an element in the tuple
print("tuple 2 is ",tuple2)
print("the number of time 10 occures in tuple 2  ",tuple2.count(10))

#5. Perform slicing on the tuple
print(tuple2[6])
print(tuple2[2:6])