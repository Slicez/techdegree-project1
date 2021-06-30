"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""


import random
# print a welcome screen 
print("Welcome to Harold Number gussing game")
username = input("Please enter your name?: ")
print("Welcome {} Lets's begin!".format(username))

def start_game():
    attempts = 1
    random_numbers = random.randint(1,10)
    users_try = 0
    while users_try != random_numbers :
        try:
             users_try = int(input("Pick a number between 1 and 10: "))
             if users_try < 1 or users_try > 10:
                print("Hold up your number must be between 1 and 10. Try again!")
                continue
        except ValueError:
                print("Hold up the number must be an interger between 1 and 10. Try again!")
        else:
            if users_try > random_numbers:
                attempts += 1
                print("The number you type is to high please try again: ")
            elif users_try < random_numbers:
                attempts += 1
                print("The number you type is to low please try again: ")
            else:
                print("You got the right number The number was {} and it took you {} tries. Good Job".format(username,random_numbers,attempts))
            return attempts

    



# Kick off the program by calling the start_game function.
start_game()

