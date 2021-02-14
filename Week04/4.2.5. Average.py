# A program to read in numbers, add them to a list and find the average of the list.
# Author: Ryan Cox


# Reading in a number and saving as the int 'number'
number = int(input("Enter a number (0 to stop): "))


# Creating a list 'numbers'
numbers = []


# Setting a loop until the user types 0. 
while number != 0:

# Adding the 'number' to 'numbers'. And then re-inputting number.
    numbers.append(number)
    number = int(input("Enter a number (0 to stop): "))


# Goes through the list and executes statements for each item temporarily defined as 'item'
for item in numbers:
    print(item)


# Finding the average of the items in numbers
# Finding the sum of the items in the list and dividing by the number of items in the list. 
average = float(sum(numbers)/len(numbers))


# alternative way to find average. 
#import numpy
#average = (float(numpy.mean(numbers)))


# Outputting average
print("The average number is {}".format(average))