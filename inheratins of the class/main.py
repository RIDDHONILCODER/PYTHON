#Write a Python program to implement Inheritance by creating a Parent Class Vehicle with a constructor that has details like name, maximum speed, and mileage. Then, create a Child Class Bus that inherits Class Vehicle. Finally, showcase Inheritance to display the details of the Vehicle Bus named - School Volvo.
#parant class
class vehicle:
    def __init__(self,name,max_speed,milage):
        self.name=name
        self.max_speed=max_speed
        self.milage=milage

class car(vehicle):
    pass
        
ob1=car("cevorlate",150,20)
print("the parant class is ",ob1.name,ob1.max_speed,ob1.milage)