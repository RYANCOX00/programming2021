# This program will read in a float number and output it as an int rounded down. 
# Author: Ryan Cox

# Reading in and converting the number to a float.
floatNumber = float(input("Please input a float number: "))


import math

# Rounding the float down to the closest whole number (int) and saving as a variable.
intNumber = (math.floor(floatNumber))


# Outputing the float and int in a sentence.  Merged through format function.
print("Your number {} rounded down to the closest whole number is {}.".format(floatNumber, intNumber))