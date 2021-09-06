# Author JJ
# Date   
# Version: 0.1
# Hot and Cold
# This program tells if it is above or below freezing
#
name = input ("What is your name?")
print ("Hello {} Welcome!". format (name))
#
# user temperature input
temperature = int(input ("What is the temperature today?"))
#
# if temperature is == 0 print freezing
if temperature == 0 :
  print ("freezing!")
#
# if temperature smaler than 0 print "below freezing"
elif temperature < 0 :
  print ("Below freezing!")
#
# if temperature bigger than 0 freezing print "above freezing"
elif temperature > 0 :
  print ("Above freezing!")
