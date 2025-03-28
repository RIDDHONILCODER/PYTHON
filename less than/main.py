#Write a program to overload the less than (<) and equal to (==) operators. For example, create objects - ob1 and ob2 with values 3 and 4 to compare values, respectively. You can additionally create more objects to try different values.
class a():
    def __init__(self,x):
        self.x=x
    
    def __lt__(self,other):
        if self.x< other.x:
            return "ob1 is less than ob2 "
        else:
            return "ob2 is less than ob1 "
    def __eq__(self,other):
        if (self.x==other.x):
            return "both are equal"
        else:
            return "they are not equal"
ob1=a(3)
ob2=a(4)
print(ob1<ob2)
print(ob1==ob2)