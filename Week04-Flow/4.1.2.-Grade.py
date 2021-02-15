# A program to determine what grade a student gets based off their percentage.
# Author: Ryan Cox


# Reading in the students result in percentage.  Converted to float as percent may not be integer. 
result = float(input("Enter the precentage: "))


# Outputing result less than 40 as a fail. 
if result < 40:
    print("Your grade is - Fail.")


# Outputting result from 40 to 49.99 as a pass. 
elif result < 50:
    print ("Your grade is - Pass.")


# Outputting result from 50 to 59.99 as a merit 1.
elif result < 60:
    print("Your result is - Merit 1.")


# Outputting result from 60 to 69.99 as a merit 2.
elif result < 70:
    print("Your result is - Merit 2")


# Outputting everything else as a distinction. i.e. 70 and over. 
else:
    print ("Your result is - Distinction")