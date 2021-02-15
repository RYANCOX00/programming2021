# A program that requires the user to guess a number until they guess correctly.
# Author:  Ryan Cox


# Reading is a number from the user and saving it as an int variable. 
userGuess = int(input("Guess a number between 1 - 100: "))

# Setting the answer to 30
correctNumber = 30


# Creating a sentinel controlled loop until the user types in 30.
while userGuess != correctNumber:
    
# Outputting "Wrong" until correctNumber is inputted and requested that the user inputs another number.
    print("Wrong!")
    userGuess = int(input("Guess again: "))

# Informing the user when they guess correctly. 
print ("Well done. The number was {}.".format(correctNumber))