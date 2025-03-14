#Write a program to create a class IOString which consists of a constructor that gives a default value to variable str1. Next up create a method that gets a string as input from the user. Create another method that will print the string in the upper case. Next up create an object and call methods to get everything implemented.

#Write a program to create a class IOString
class IOString:
    def __init___(self):
        self.str1= ""
        print("constricting an object")
    def getstring(self):
        self.str1=input("enter a string")
    def printstring(self):
        print("the string in upper case is ",self.str1.upper())
    def __del__(self):
        print("destroying the object")
object=IOString()
object.getstring()
object.printstring() 
      