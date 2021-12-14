import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

# importing random (computer choice)

userchoice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if userchoice == 0:
    print(rock)
elif userchoice == 1:
    print(paper)
elif userchoice == 2:
    print(scissors)
else:
    print("You need to choose between 0, 1 or 2")

# Randoming computer choice

print("Computer choose")

computerchoice = random.randint(0, 2)

# transforming computer choice to image

if computerchoice == 0:
    print(rock)
elif computerchoice == 1:
    print(paper)
else:
    print(scissors)

# result of the battle!!

if userchoice == 0 and computerchoice == 0:
    print("Draw!")
elif userchoice == 0 and computerchoice == 1:
    print("You loose!")
elif userchoice == 0 and computerchoice == 2:
    print("You win!")
elif userchoice == 1 and computerchoice == 0:
    print("You win!")
elif userchoice == 1 and computerchoice == 1:
    print("Draw!")
elif userchoice == 1 and computerchoice == 2:
    print("You win!")
elif userchoice == 2 and computerchoice == 0:
    print("You loose!")
elif userchoice == 2 and computerchoice == 1:
    print("You win!")
elif userchoice == 2 and computerchoice == 2:
    print("Draw!")

else:
    print("Can\'t compare, you didn't typed a valid number!")
