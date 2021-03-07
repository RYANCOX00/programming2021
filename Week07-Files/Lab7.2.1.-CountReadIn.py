# A program that reads in a number and saves it to an external file, overwriting the contents 
# eachtime the program is ran.
# Author: Ryan Cox 


def writeNumber(number): # Creating function that accepts one arguement
    file = "count.txt" 
    with open (file, "wt") as f: # The mode is writing i.e. creates a file and writes or over-writes an existing file.
        number = f.write(str(number))  # Text file is in string format
        return number

writeNumber(10) # Running the function with an arguement pre-defined. 