# A program to list the months of the year and output the summer months as a new list.
# Author: Ryan Cox

# Creating a tuple containing the months of the year.
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

# Creating a new tuple with the summer months only. 
summer = months[4:7]

# creating a loop to print out summer months seperately.
for month in summer:
    print(month)