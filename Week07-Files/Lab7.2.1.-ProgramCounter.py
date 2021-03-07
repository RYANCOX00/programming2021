# A program that we tell a user how many times a program was ran. 
# Author: Ryan Cox

file = "count.txt"

import os

def creatingFile():
    if not (os.path.exists(file)):
        with open(file, "xt") as f:  # Creating file if it does not exiting.
            print("File created")
        with open(file, "w") as f: # Adding 0 to the file, otherwise int below cannot be read in at line 16.
            f.write(str(0))

def readNum():
    with open(file, "rt") as f: 
        num = int(f.read()) # Reading in the amount of times the program already ran as an int.
        return num  # Returning the amount.

def writeNum(number):
    with open(file, "wt") as f:
       f.write(str(number)) # writing the new amount to the file as a string. 
       
creatingFile()
num = readNum()  # Running the function defined above.
num = int(num)
num += 1 # Adding one to the previous amount of times ran. 
print ("We have run this program {} times".format(num))
writeNum(num) # Running the function defined above. 