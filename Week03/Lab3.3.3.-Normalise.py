# Reading in a string from a user and normalising their input.
# Author: Ryan Cox


# Reading in a string and striping the white space and making it lower case.
rawString = input("Please enter a string: ")
stripedString = rawString.strip().lower()


# Counting the characters of both the raw string and the normalised string.
countRaw = len(rawString)
countStriped = len(stripedString)


# Outputting the data to the user.  
# The variables were merged to strings using format function. 
print("Your string has been normalised to {}.".format(stripedString))
print("Your string had {} characters. The normalised string has {} characters.".format(countRaw,countStriped))