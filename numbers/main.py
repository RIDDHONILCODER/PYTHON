num1=int(input("enter a number 1   "))
num2=int(input("enter a number 2   "))
choice=int(input("1.add 2.subtract 3.multiply 4.divide   "))

def add(x,y):
    return x+y;

def subtract(x,y):
    return x-y;
def multiply(X,y):
    return x*y;
    
if choice==1:
    num3=add(num1,num2)
    print("the result is ",num3)
elif choice==2:
    num3=subtract(num1,num2)
    print("the result is ",num3)
elif choice==3:
    num3=multiply(num1,num2)
    print("the result is ",num3)

