# A program to generate 10 random numbers between 0 and 100 and save into a list and,
# also print the highest three. 
# Author: Ryan Cox

# Creating the list.
randomList = []


import random

# Defining the loop variable. The loop will run until their is 10 items in the list.
# Also generating a random number between 0 to 100, and adding it to the list.
while (len(randomList) < 10):
    randomNumber = (random.randint(0,100))
    randomList.append(randomNumber)

# Sorting the list and saving the top three as a varibale
topThree = (sorted(randomList)[-3:])


# Outputting the results
print ("Ten random numbers are: \t\t{}".format(randomList))
print ("The top three are: \t\t\t{}".format(topThree))