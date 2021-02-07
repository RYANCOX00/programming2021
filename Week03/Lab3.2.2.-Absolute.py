# This program takes is a vlaue and coverts it to its absolute value.
# Author:  Ryan Cox


# The question did not specify whether it should be an int or float.  We will assume that it should be a float. 
# Reading in the number and converting it to a float.
rawNumber = float(input("Please enter a number: "))


# Finding the absolute value of the number.
absolutNumber = abs(rawNumber)


# Outputting the first number and its absolute value in a sentence.  They are inputted using format.
print("Your first number was {}. The absolute value of it is {}".format(rawNumber,absolutNumber))