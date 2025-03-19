#Write a program to create a parent class Person (attributes - name, id number) with a method display to display the attributes. Next, create a child class Employee (attributes - name, id number, salary, post). Access the attributes of parent class in child class. Then, create an object for child class and call the display method to display the name and id number.
class person:
    def __init__(self,name,id_number):
        self.name=name
        self.id_number=id_number
    def display(self):
        print("the name is this ",self.name)
        print("the id_number is this ",self.id_number)
class employe(person):
    def __init__(self,name,id_number,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,id_number)
        
ob1=employe("riddhonil",6969,50000,"manager")
ob1.display()