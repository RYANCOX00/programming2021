# I am writing an application at the moment, in it I take an input of an amount
# in the form -9.44 (9 dollars and 44 cent), the issue there may or may not be a
#minus sign, and the bank takes in the amount in cent, (944). Write a program
#called convert.py that takes in a float amount of dollars, and returns that
#absolute amount in cent.

import math


# Reading in currency as a float, ensuring it is an absolute value and saving such as a variable.
moneyIn = abs(float(input("How much money was received in euro and cent: ")))


# Converting the value received to a whole number (int) as cents. Multiplied by 100 
# We needed to use math.ceil up to prevent it from being rounded down when coverted to int. 
centIn = int(math.ceil(moneyIn*100))


# The results are outputted.  The variables are merged to the string using the format function. 
print ("The amount received: €{}, equals to {} cents.".format(moneyIn,centIn))