class vehicle:
     def __init__(self,name,max_speed,milage):
         self.name=name
         self.max_speed=max_speed
         self.milage=milage
 
class car(vehicle):
     pass
         
ob1=car("volvo",150,50)
print("the parant class is ",ob1.name,ob1.max_speed,ob1.milage)