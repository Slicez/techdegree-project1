"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""


import random
# print a welcome screen 
print("Welcome to Harold Number gussing game")


def start_game():
    attempts = 1
    guess = random.randint(1,10)
    tries = 0
    while tries != guess:
        try:
            tries = int(input("Pick a number between 1 and 10: "))
            if tries < 1 or tries > 10:
                print("The number must be between 1 and 10 please try again!")
                continue
        except ValueError:
            print("The number must be an interger between 1 and 10. Try again")
        else:
            
            if tries > guess:
                attempts += 1
                print("Your guess is to high! Try again: ")
            elif tries < guess:
                attempts += 1
                print("Your guess is to low! Try again: ")
    else:
         print("You got the right number!")
    return attempts



# Kick off the program by calling the start_game function.
start_game()



