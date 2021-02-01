# Reading in a number, converting and adding a number.  Formatting to make them compatiable with strings.

# Reading in a number as a string, converting it to a int. 
number = int(input("Enter a number?"))

# Adding a number to that int and creating a int as a variable "new number"
newnumber = (number + 154)

# Formating to place the int into a sentence for print
print("Lets add 154 to {} and make that equal {}" .format (number,newnumber))