# A program to determine whether a number is odd or even.
# Using a sentinel loop to exit. 
# Author: Ryan Cox


# Reading in a number from a user. Converting from str to int.
# Initialising the loop 
number = int(input("Please enter an integer number (-1 to quit): "))


# Adding the loop exit condition i.e. the loop will run until -1 is typed. 
while number != -1:

# Calculating if the number is divisible by 2. If true, the user will be notified that the number is even.
    if((number % 2) == 0):
        print("{} is even".format(number))

# If not divisible by 2, the number is odd.  If this is the case, the user will be notified that the number is odd.
    else: 
        print("{} is odd".format(number))



# Varibale continues to be inputted until -1 is typed. 
    number = int(input("Please enter an integer number (-1 to quit): "))