# Reading in a two numbers to for division and giving the integer answer and the remainder. 
# Author: Ryan Cox


# Reading in two numbers as integers
x = int(input("Please enter a number : "))
y = int(input("Enter a number to divide into the first number: "))

# Preforming the math to find the integer answer and the remainder. 
intAnswer = x//y
remainder = x%y

# Outputing the solution to the user. 
# Formating the variables to allow integers to print with strings
print("{0} divided into {1} is {2}, with {3} remaining.".format(x,y,intAnswer,remainder))