import random
#This game playes with three simple role
# 1-Rock wins against scissores
# 2-Scissors win against paper
# 3-Paper wins against rock
# Rock

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

option = int(input("Enter 1 for rock, 2 for paper, 3 for scissors \n "))

com_option = random.randint(1,3)
if option == 1 or option == 2 or option == 3: #the user must enter 1, 2 or 3 nothing out of them

    #print the user choice
    if option == 1:
        print(f"Your Choice : \n {rock} \n ")
    elif option == 2:
        print(f"Your Choice : \n {Paper} \n ")
    elif option == 3:
        print(f"Your Choice : \n {Scissors} \n ")

    #print the computer choice
    if com_option == 1:
        print(f"Computer Choice : \n {rock} \n ")
    elif com_option == 2:
        print(f"Computer Choice : \n {Paper} \n ")
    elif com_option == 3:
        print(f"Computer Choice : \n {Scissors} \n ")

    #judges the winner or loser
    if (option == 3 and com_option == 2) or (option == 2 and com_option == 1) or (option == 1 and com_option == 3):
        print("You lose")
    else:
        print("You Win!")
else:
    print("you have entered wrong option! ")