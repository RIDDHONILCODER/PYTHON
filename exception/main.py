#Write a program to check how the exceptions and finally statement works
try:

   n1,n2=eval(input("enter 2 numbers saperated by a coma"))
   resoult=n1/n2
   print(resoult)
except ZeroDivisionError:
    print("can not divied by 0")  
except SyntaxError:
    print("you have forgoten to put a coma ")  
except:
    print("their is some error")      
finally:
    print("their is no error")    