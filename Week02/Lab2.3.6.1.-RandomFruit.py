# Printing out random fruit from a list.  
# Author: Ryan Cox

fruits = ["apple", "banana", "orange", "pear"]

import random


# This function is generating a number 0 to 3 (or the range may increase if more fruits are added).
# len(fruits) gets the total number of fuits in the variable(4), -1 because the the range starts at 0, thus ending at 3. 
index = (random.randint(0, len(fruits)-1))


# This lien will use the random number created for index above, and will output that assigned fruit within the range as save it as "fruit". 
fruit = fruits[index]

# No need to format as the variable is a string already and its at the end so easy to add. 
print("The random fruit chosen for you is "+fruit)