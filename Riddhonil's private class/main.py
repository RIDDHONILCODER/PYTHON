#Write a program to create a class with following variables and methods - 1. Private variable named privateVar that contains an integer value 2. Create a private function privMeth that prints a message 3. Create a function hello that prints the value of privateVar 4. Create an object for the class and call all the functions.
class Riddhonil:
    __privateVar=2
    def __privMeth(self):
        print("this is the Private method")
    def hello(self):
        print("the value of privatevar is this ",Riddhonil.__privateVar)
        
ob=Riddhonil()
ob.hello()
ob.__privMeth()