# A program to determine what grade a student gets based off their percentage.
# Following on from Grade.py, this program will round up the percentage for results 
# that are .5 off the next highest grade.
# Author: Ryan Cox


# Reading in the students result in percentage.  Converted to float as percent may not be integer. 
result = float(input("Enter the precentage: "))


# Rounding up the percentage for results that are .5 off the next highest grade. 
import math

if result >=39.5 and result <40:
    result = math.ceil(result)

elif result >=49.5 and result <50:
    result = math.ceil(result)

elif result >=59.5 and result <60:
    result = math.ceil(result)

elif result >=69.5 and result <70:
    result = math.ceil(result)
    


# Outputing result deemed a fail, pass, merit 1, merit 2, or distinction. 
if result < 40:
    print("Your grade is - Fail.")
    
elif result < 50:
    print ("Your grade is - Pass.")

elif result < 60:
    print("Your result is - Merit 1.")

elif result < 70:
    print("Your result is - Merit 2")
 
else:
    print ("Your result is - Distinction")