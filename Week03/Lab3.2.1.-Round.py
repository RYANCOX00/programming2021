# This program will read in a float and output it rounded as an integer.
# Author: Ryan Cox


# Reading in an number from a user and converting it to a float. 
floatnumber = float(input("Please enter a number as a float: "))


#Rounding the float to the closest whole number and coverting to an integer.
intNumber = int(round(floatnumber,0))


# Outputting the results to the user using format.
# This is the most suitable way as there is multiple variable types within the sentence. 
print ("Your float number was {}. This number rounded to the closest int is {}.".format(floatnumber,intNumber))