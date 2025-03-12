#Write a program to create a class Vehicle and perform the following tasks - 1. Create an __init__ method with arguments - max_speed and mileage 2. Create an object of class Vehicle and pass the maximum speed and mileage of the car 3. Print the values of max_speed and mileage by using the object
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
lamborgini=Vehicle(300,20)
bmw=Vehicle(250,20)
print("the max speed of lamborgini is ",lamborgini.max_speed)
print("the max speed of bmw is ",bmw.max_speed)
print("the mileage of lamborgini is ",lamborgini.mileage)
print("the mileage of bmw is ",bmw.mileage)