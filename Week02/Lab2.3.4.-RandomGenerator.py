# Writing a program that prints a random number between a range defined by user. 
# Author: Ryan Cox

# Asking the user to input the lowest and highest number of the range.
# Also input is converted to an int so that we can generate the range.
firstNumber = int(input("Enter the first number of the range: "))
lastNumber = int(input("Enter the last number of the range: "))


import random

# Generating a random number and saving it as variable "number".
number = (random.randrange(firstNumber,lastNumber))


# Telling the user what the random numebr is.  
# It is required to format the number as it is currently an int.  
print("Your random number between your range is {}".format(number))