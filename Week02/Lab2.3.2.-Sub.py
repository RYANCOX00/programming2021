# This program read in two number and will subtract one number from the other number.
# Author: Ryan Cox


# Reading in the numbers from the user. 
# We also need to covert the data to int to preform the math below.
x = int(input("Please enter a number: "))
y = int(input("Enter another number: "))


# Doing the math and saving the answer as a varibale
answer = x - y


# Putting the data into a sentence using the format function. 
# Allows str and int to be combined
print( "{} minus {} equals to {}".format(x, y, answer))