
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