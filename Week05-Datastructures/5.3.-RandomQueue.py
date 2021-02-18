# A program to remove numbers from a queue one at a time. 
# Author: Ryan Cox

import random

randomQueue = []
rangeUpTo = 100
amount = 10


# Setting the amount of random Int to be generated
for number in range(0,amount):
    # Generating the random int and adding it to the list.
    number = random.randint(0,rangeUpTo)
    randomQueue.append(number)


# Printing the 10 random ints.
print ("Queue is ", randomQueue)


# While the list does not equal to zero, keep applying the below statements
while len(randomQueue) != 0:
    # Creating a loop for items in randomQueue
    for extract in randomQueue:
        # Permanently extracting the first number and saving it as a variable. The variable will be replaced once loop occurs
        extract = randomQueue.pop(0)
        print("Current number is ", extract, " and the queue is ", randomQueue)
   
    
# Once all items are extracted from the list, outputing such to the user.
print("the queue is now empty")