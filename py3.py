# Author: JJ
# Date: 3 April 2020
# Version: 1.0
#
# Math Quest

# Ask student to enter name and enter the timestable they want to practice
print ("Welcome to Math Quest")
print ("What is your name?")
name = input()
print ("Hello {} which timestable would you like to practice, from (1-12)?". format (name))
number = input()
print ("Ok {}, on a piece of paper, write down the {} times table from 1 to 12 and I’ll show you the answer so you can check your work.". format (name, number))

# enter 'y' for student to begin
userInput="n"
while(userInput=="n"):
    userInput=input("Are you ready? (Enter'y'to start)")

# enter the number for timestable
timestable = int (input("enter the number:"))
for number in range (1,13):
    print (timestable, "*", number, "=", timestable*number)

# asks how the student did with the practice
answer = input("Did you get them all correct?(y/n)")
Y = "Great job!"
N = "No? Better luck next time"
T = " Thanks for playing Maths Quest."
if (answer =="y"):
    print (Y+T)
else:
    print (N+T)
    