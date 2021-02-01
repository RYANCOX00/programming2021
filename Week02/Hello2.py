# Reading in a users name and greeting them
# Author: Ryan Cox

# Greeting with Hello and inputted name
name = input ("Enter you name: ")
print ("Hello " + name) 


# Greeting with Hello + inputted name, and nice to meet you on a new line
print("Hello " + name + "\nNice to meet you")


# Alternatively you could print this with the format included to ensure its compatable
print("Hello {} \nNice to meet you" .format(name))
