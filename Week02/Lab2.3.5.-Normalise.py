# Reading in a string from a user and normalising their input.
# Author: Ryan Cox


trailingSpaces = input("Enter a statement with trailing spaces: ")

# Removing the white spaces and making the string lower case. 
amendedText = trailingSpaces.strip().lower()


# Counting the characters of the 'trailingSpaces' and 'amendedText' variables.
countTrailingSpaces = len(trailingSpaces)
countAmendedText = len(amendedText)


# Outing the normalised text and telling the user how many chartacters were saved. 
# We used the format function to input the number variables as they needed to be merged with strings. 
print ("This is your text normalised: " +amendedText)
print ("Your original text had {} characters, now it has {} characters with the same message.".format(countTrailingSpaces, countAmendedText))