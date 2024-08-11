""" SNAKE WATER GUN GAME """

import random

def game_function():
    print("Welcome to Snake Water Gun Game")

    playerInput = input("Enter your choice (Snake, Water or Gun):  ")
    computerInput = random.choice(["Snake", "Water", "Gun"])

    print(f"You choose {playerInput} and computer choose {computerInput}")

    if playerInput == computerInput:
        print("The Game is Draw")
    elif playerInput == "Snake" and  computerInput == "Water":
      print("You Won the Game")
    elif playerInput == "Water" and computerInput == "Snake":
       print("You Lose the Game")
    elif playerInput == "Gun" and computerInput == "Water":
       print("You Won the Game")
    elif playerInput == "Snake" and computerInput == "Gun":
       print("You Lose the Game")
    else:
       print("You Lose the Game")

answer = game_function()
print(answer)