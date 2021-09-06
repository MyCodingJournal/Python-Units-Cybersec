# This are exercises from Term 1
# JJ Revision session
# Date: 3/6/2020
# Session 1 exercises

################## Part 1 session 1 ####################

print("Hello, world!")
name = input("What is your name?") 
print("Hello", name) 
print("This looks like it should work, but it’s missing two important characters") 
print("This one is extra tricky. What's wrong here?")
print("How do I make this line work?") 
day = int(input("What day is it? [e.g. for March 26, type 26]")) 
month = input("What month is it? [e.g. for March 26, type March]") 
print("In Australia, this is written: ", day, "-", month)


################## Part 2 Session 1 #####################

# This program output canada day on the screen

canadadaydate = input("When is the date of Canada day? " )
print ("Canada day is on", canadadaydate)

Australia_day = input ("When is Australia day? ")
print ("Australia day is on", Australia_day)

age = "116"
print ("The oldest person alive is Emma Morano, and she is",age)

#or

print ("The oldest person alive is Emma Morano, and she is \t 116")
print ("The oldest person alive is Emma Morano, and she is 116 ")


# This program adds 3 numbers

print ("Please enter 3 numbers. ")
numb1 = int (input("Enter first numner: "))
numb2 = int (input("Enter second number: "))
numb3 = int (input("Enter third number: "))
sum = numb1 + numb2 + numb3
print (sum)


# or ( # + / *)

print ("Please enter 3 numbers. ")
numb1 = int (input("Enter first numner: "))
numb2 = int (input("Enter second number: "))
numb3 = int (input("Enter third number: "))
print ("The sum of these number is: ", numb1 + numb2 + numb3)


# This program ask for you name and age

name = input(" What is your name? ")
age = input ("What is your age? ")
print ("Your name is", name)
print ("Your age is", age)


# This program ask for the city you were open

city = input ("What was the city you were born in? ")
print ("I bet you were born in", city, "am i right?")


# This program ask for the address user 

street = input ("Enter the street you live in: ")
suburb = input ("Enter the suburb you live in: ")
state = input ("Enter the state you live in: ")
postcode = input ("Enter the postcode you live in: ")
print (street)
print (suburb)
print (state)
print (postcode)


# This program ask for your date of birth

dateofbirth = input("Enter DOB in this order dd\mm\yyyy: ")
print ("Your date of birth is",dateofbirth)


################ Session 2 Exercise 2 ##################

###Handling different data types in python###

a = 1
b = 2
sum = a + b
print ("The sum total of a + b is", a + b)
print ("The sum total of a + b is", sum)

# print ("The sum total of a + b is" + a + b )
# print ("The sum total of a + b is" + sum)
# This will not work because you can only concatenate string not integer, Plus '+' tells it to concantenate.
# + operator is a concatenation & math operator.

yourNumber = int(input("Enter your number of choice...."))
# coverting input into an integer.
print ("I will add 100 to your number and print....")
newNumber = yourNumber + 100
print ("The new number after adding your number is",str (newNumber)) 
# 'str()' to turn integer into a string

# another example

YourNumber = input("Enter any number of your choice....")
print ("I'll concatenate 100 to your number and will print....")
newNumber = YourNumber + "100" # making the 100 into a string by  using " "
print ("The new number after adding 100 to your number is " + newNumber
) 

# than concatenation '+' is possible here.

# In conclusion you can only add or concatenate data source of the same type.

# Result = A + C (TypeError: unsupported operand type(s) for +: 'int' and 'str')

A = 2
B = 3
C = "Boxhill"
Result = A + B
print ("The result is", Result)
print ("The result is " + str (Result))
print (f"My results at {C} is", Result) 

# String function from LPTHW! just to test knowledge. Yay!

###Conditional Statements or conditionals###

l = 10
b = 5
AreaOfRectangle =  l * b
print (f"The are of rectangle is {AreaOfRectangle}")
print ("The are of rectangle is " + str(AreaOfRectangle))
print ("The are of rectangle is", str(AreaOfRectangle))
print ("The area of rectangle is", l * 5 )

# are of rectangle

L = int(input("Enter the length of rectangle..."))
B = int(input("Enter the breath of rectangle..."))
AreaOfRectangle = L * B
print ("The are of rectangle is ", L * B)

# area of circle

Pi = 3.14
R = int(input("Enter the radius of circle..."))
AreaOfRectangle = Pi * R * 2
print ("The total area of circle is", Pi * R * 2)

# Conditional statements and conditionals (if, elif, else)
# The script compares 2 numbers input bu user

# Input statments
FirstNumber = int(input("Enter first number..."))
SecondNumber = int(input("Enter second number..."))
# conditional statements
if (FirstNumber>SecondNumber): # first condition
  print ("The first number you entered is greater than the second.") 
  # This block of code will run if expression inside if() returns True.
elif (FirstNumber<SecondNumber): # second condition
  print ("The second number you entered is greater than the first.")
  # This block of code will run if expression inside elif() returns Truie.
else: # no need of expression-covers all cases accept if() and elif()
  print ("The two numbers you entered are equal.")
  # This block of code will run if both expressions inside if() and elif() returns false.

# trying out a simple yes no condition!
# the code didnt run previously because i need to define yes with ""

rain = input("Is it raining now?, answer yes or no: ")
if (rain == "yes"):
  print ("Go home!")
else:
  print ("Yay! let's go out!")

# This script calculates fee payment for extra weight/baggauge.

weight = float(input("How many pounds does your suitcase weigh? "))
if (weight > 50):
  print ("There is a $25 charge for heavy luggage...")
else:
  print ("You are good to go.")
print ("Thank you for your business!")

# This script tells the user if input is negative or positive.

Number = int(input("Enter your number..."))
if (Number > 0):# first condition
  print ("This is a positive number.")
  print ("That means this is greater than 0.")
  # This block will run if the expression inside if() returns True.
elif (Number == 0):# second condition
  print ("You typed zero.")
  # This block will run if the expression inside elif() returns True.
else:# no need for expression, covers all accept if() and elif()
  print ("This is a negative number.")
  print ("That means it is less than 0.")
  # This block will run if both expressions inside if() and elif() returns false.

# Advanced Conditionals Nested If statement.
# i.e if statement inside another if statement.
