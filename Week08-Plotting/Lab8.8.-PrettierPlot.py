# A program that will show the salary and age of a particular person (random). 
# Author: Ryan Cox

import numpy as np
import matplotlib.pyplot as plt

# Setting the parameters for the salaries and ages. 
lowestSalary = 2000
highestSalary = 8000
number = 10
minAge = 21
maxAge = 65

# Creating variable for ages and salaries
np.random.seed(1) # Storing the random numbers after the first generation. 
salaries = np.random.randint(lowestSalary, highestSalary, number) # Generating random salaries based on parameters above.
ages = np.random.randint(minAge,maxAge,number) # Generating random ages based on parameters above.
colour = np.array([55, 34, 12, 99,78,44,22,66,88,3]) # Assigning each entry a color. 


# Creating variables for a line
xData = np.array(range(1,101)) # Setting the x axis value to 1-100.
yData = xData * xData # y is (x squared). 


plt.scatter(ages, salaries, marker = "o", c= colour, cmap="Accent", s= 100, label ="Salaries") # Plotting as O's, colors from pastel map, and size of each as 100.
plt.xlabel("x Axis") # labeling the x axis
plt.ylabel("y Axis") # labeling the y axis
plt.plot(xData,yData, c="k", label = "Line") # adding a black line and label (for legend)
plt.legend()

plt.show() # running the plot. 
plt.savefig('prettier-plot.png')