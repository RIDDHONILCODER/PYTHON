#Write a program to check how many times a character is repeated in a word?

word=input("enter a word ")

char=input("enter a character you want to find in the word ")

lenth=len(word)

count=0

for i in range (0,lenth):
    if word[i]==char:
        count=count+1
print("The number of occurence of the letter {} in the word {} is {} times".format(char,word,count))
