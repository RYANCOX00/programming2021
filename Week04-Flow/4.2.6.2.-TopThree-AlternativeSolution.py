# Andrews solution to Top Three - for practice
# Author: Ryan Cox


# Creating a list
randomList = []


# Defining the elements of the question.  Clever if you wish to easily make an amendment later. 
lowestNumber = 0
highestNumber = 100
howMany = 10
highest = 3

import random


# Creating a for loop.  For 10 numbers, generate them randomally between the defined range and add them to 'randomList'
for number in range(0,howMany):
    number = random.randint(lowestNumber,highestNumber)
    randomList.append(number)

print ("{} random numbers:\t\t{}".format(howMany,randomList))


# Creating a copy of the original list. 
topOnes = randomList.copy()

# Sorting the new list in reserve. reverse = True
topOnes.sort(reverse= True)

# Then print - note the range of topOnes printed.
print ("The top {} numbers are:\t\t{}".format(highest,topOnes[0:3]))