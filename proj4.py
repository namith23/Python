#rock, paper and scissors game
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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print("You chose")

print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose: {computer_choice}")
print(game_images[computer_choice])

if 3 < user_choice < 0:
    print("You chose invalid number. Computer win")
elif user_choice == 0 and computer_choice == 1:
    print("Computer win")
elif user_choice == 1 and computer_choice == 2:
    print("Computer win")
elif user_choice == 1 and computer_choice == 0:
    print("Computer win")
elif user_choice == 2 and computer_choice == 1:
    print('You win')
elif computer_choice == 2 and user_choice == 0:
    print("You win")
elif user_choice == computer_choice:
    print("DRAW")
else:
    print("no win")