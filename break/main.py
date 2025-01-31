#Write a program to check alphabet “A” is present in the given string or not. And terminate the loop after finding the alphabet “A.”
word=input("enter a word")

for i in word:
    if i=='A' or i=='a':
        print("found a ")
        break
    else:
        print(i)