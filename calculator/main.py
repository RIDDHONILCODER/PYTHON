#Write a program to make a calculator : For making a calculator create four functions add, subtract, multiply, divide. Ask for a choice from users which operation they want to perform. Take user input whatever operation they want to perform And call that function accordingly.

def add(n1,n2):
    print("{}+{}={}".format(n1,n2,n1+n2))

def subtract(n1,n2):
    print("{}-{}={}".format(n1,n2,n1-n2))

def divied(n1,n2):
    print("{}/{}={}".format(n1,n2,n1/n2))

def multiply(n1,n2):
    print("{}*{}={}".format(n1,n2,n1*n2))


print("1.add")
print("2.subtract")
print("3.divied")
print("4.multiply")

number1=int(input("enter the first number"))

number2=int(input("enter the secend number"))

choice=int(input("enter your choice"))

if choice==1:
    add(number1,number2)
if choice==2:
    subtract(number1,number2)
if choice==3:
    divied(number1,number2)
if choice==4:
    multiply(number1,number2)


