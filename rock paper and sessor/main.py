import random
choice=input("rock,paper or sessor")
computer_choice=["rock","paper","sessor"]
choice_of_computer=random.choice(computer_choice)
if choice==choice_of_computer:
    print("its a tie")
elif choice=="rock":
    if choice_of_computer=="sessor":
        print("rock smashed sessor so you win")
    else:
        print("paper has coverd you so you lose") 
elif choice=="paper":
    if choice_of_computer=="rock": 
        print("you win")        
    else:
        print("you lose")  
elif choice=="sessor":
    if choice_of_computer=="rock": 
        print("you lose")        
    else:
        print("you win")              