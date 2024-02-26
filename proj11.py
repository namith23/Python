#Number guessing game

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
print(logo)
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
        if guess > answer:
                print('Too High')
                return turns -1
        elif guess < answer:
                print("Too low")
                return turns -1
        else:
                print("You got it. The answer is {answer}")

def set_difficulty():
        level = input("Choose the difficulty. Type 'easy' or 'hard':")
        if level == 'easy':
                return EASY_LEVEL_TURNS
        else:
                return HARD_LEVEL_TURNS

def game():
        print("Welcome to the number guessing game:") 
        print("I'm thinking of number between 1 amd 100")
        answer = randint(1, 100)
        turns = set_difficulty()
        guess = 0 
        while guess != answer:
                print(f"You have {turns} atempts remaining to guess the number")
                guess = int(input("Make a guess:"))
                turns = check_answer(guess, answer, turns)
                if turns == 0:
                        print("you loose")
                        return
                elif guess != answer:
                        print("Guess again")
game()