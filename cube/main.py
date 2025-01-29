#Define a function to find a cube and define another function which let execute the cube function if the number is divisible by 3
def divisible_by_3(c):
    if c%3==0:
        print("the number is divisible by 3 ")
    else:
        print("the number is not divisible by 3")
        
def cube(num):
    c=num*num*num
    print("the cube of the number is ",c)
    divisible_by_3(c)

num=int(input("enter a number"))
cube(num)



