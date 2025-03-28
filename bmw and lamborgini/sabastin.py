class bmw():
    def milage(self):
        print("bmw's milage is 250")
    def speed(self):
        print("bmw's speed is 160")
class lamborgini():
    def milage(self):
        print("milage of lamborgini is 250")
    def speed(self):
        print("lamborgini's speed is 300")
        
ob1=bmw()
ob2=lamborgini()
for i in (ob1,ob2):
    i.milage()
    i.speed()
    
