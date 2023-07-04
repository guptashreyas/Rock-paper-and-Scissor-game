import random
while True:
    
    print("Welcome to Rock Paper Scissor")
    user_score=0
    computer_score=0
    ties=0
    
    name=input("enter your name:")
    print("""
    Winning Rules:
    1.Paper vs Rock ,Paper wins
    2.Rock vs Scissors,Rock wins
    3.Scissors vs Paper,Scissors wins""")
    print()
    
    print("""Choices are:
       1.Rock
       2.Scissors
       3.Paper""")
    print()
       
    choice=int(input("enter your choice from 1-3:"))
    print( )
    while choice>3 or choice<1:
        choice=int(input("enter valid input"))
        
        
    if choice==1:
        user_choice="Rock"
    elif choice==2:
        user_choice="Scissors"
    else:
        user_choice="Paper"
    
    print("its user choice--",user_choice)
    print("now its computer turn")
    computer=random.randint(1,3)
    if computer==1:
        computer_choice="Rock"
    elif computer==2:
        computer_choice="Scissors"
    else :
        computer_choice="Paper"
    print("its computer choice--",computer_choice)
    
    if((user_choice=="Paper" and computer_choice=="Rock")or(user_choice=="Rock" and computer_choice=="Paper")):
        print("Paper wins")
        result="Paper"
    elif((user_choice=="Scissors" and computer_choice=="Rock")or(user_choice=="Rock" and computer_choice=="Scissors")):
        print("Rock wins")
        result="Rock"
    elif(user_choice==computer_choice):
        print("its a tie")
        result="tie"
    else:
        print("Scissors wins")
        result="Scissors"
        
    if result=="tie":
        ties=ties+1
    elif result==user_choice:
        print("user wins")
        user_score+=1
    else:
        print("computer wins")
        computer_score+=1
    print("scores are")
    print("userscores is-",user_score)
    print("computerscore is-",computer_score)
    repeat=input("do you want to play again(Enter 'yes' or 'no'):")
    if repeat=="No"or repeat=="NO" or repeat=="no":
        break
