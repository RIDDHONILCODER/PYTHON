#Write a program to create a class with the named employee and create a constructor and . Then, write a function to create an object for that class and delete the object. Make sure you call the function to get everything implemented!
class employe:
    def __init__(self):
        print("constructor called ")
    def __del__(self):
        print("destructor called ")
object=employe()