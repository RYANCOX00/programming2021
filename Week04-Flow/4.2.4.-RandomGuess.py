
# Reads in a number and sets the input as a variable. 
userGuess = int(input("Guess a number between 1 - 100: "))

import random
# Running a random number and saving it as the correct number.
correctNumber = random.randint(1,100)


# Creating a sentinel controlled loop until the user types the correct number.
while userGuess != correctNumber:


# If user guess is incorrect, prompting the user on whether their guess was too low or too high.
    if userGuess < correctNumber:
        print("Your guess was too low.")

    elif userGuess > correctNumber:
        print("Your guess was too high.")


# If the users guess was incorrect, asking the user to guess again.      
    userGuess = int(input("Guess again: "))


# Informing the user when they guess correctly. 
print ("Well done. The number was {}.".format(correctNumber))