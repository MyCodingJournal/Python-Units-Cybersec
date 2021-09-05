# Author: JJ
# Date: 3 April 2020
# Version: 1.0
#
# Rock Paper Scissors Game  
# 2 Players

print ("Welcome to the Rock, Paper, Scissors Game!")
print ("Lets begin!!!")

# ask players for their names and their inputs
print ("Player 1, what is your name?")
name1 = input ()
print ("Player 2, what is your name?")
name2 = input ()

print ("Hello {} and {}, welcome to the game!". format (name1, name2))

# player 1 input 
while True:
    p1 = input ("Enter player 1 choice:")

    if p1 == "r" or p1 == "p" or p1 == "s":
        break
    else:
        print ("Incorrect input")

# player 2 input
while True:
    p2 = input ("Enter player 2 choice:")

    if p2 == "r" or p2 == "p" or p2 == "s":
        break
    else:
        print ("Incorrect input")

if p1 == p2:
    print ("We have a draw, great game!")

elif p1 == "r":
    if p2 == "p":
        print ("Player 2 Wins!")
    else:
        print ("Player 1 Wins!")