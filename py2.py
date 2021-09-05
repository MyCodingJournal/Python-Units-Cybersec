# Author: JJ
# Date: 3 April 2020
# Version: 1.0
#
# Guess the random number game
# One player vs. the computer    

import random
number = random.randint(1, 6)

# ask the user for their name and their Guess
print ("What is your name?")
name = input ()
print ("Hi," + name + "!")
print ("Enter a number between: 1 and 6")
guess = int(input("What is your guess?"))

# Generates a random number and tells player lost or won 
while guess != number:
    print (" You LOST! Keep guessing!")
    guess = int(input("What is your guess?"))
else:
    print ("You Won! Congratulations!")

print ("Thank you for playing the game!")