#  A program to determine whether a number is odd or even.
# Author: Ryan Cox


# Reading in a number from a user. Converting from str to int. 
number = int(input("Please enter an integer number: "))


# Calculating if the number is divisible by 2. If true, the user will be notified that the number is even.
if ((number % 2) == 0):
    print("{} is even".format(number))


# If not divisible by 2, the number is odd.  If this is the case, the user will be notified that the number is odd.
else: 
    print("{} is odd".format(number))