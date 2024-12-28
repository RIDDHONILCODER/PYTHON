#Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed


choice=input("do you have a medical cause ‘Y’ for yes and ‘N’ for no")
attendance=int(input("Enter the attendance"))
if choice=='Y'or choice=='y':
    print("you are allowed to take the exam")
elif choice=='N' or choice=='n':
    if attendance>75:
        print("you are allowed to take exam")
    else:
        print("you are not allowed")
else:
    print("check what have you enterd")