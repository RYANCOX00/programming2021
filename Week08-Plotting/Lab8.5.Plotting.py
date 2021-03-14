# A program that will plot a simple data.
# Author: Ryan Cox

import numpy as np
import matplotlib.pyplot as plt


xData = np.array(range(1,101)) # Setting the x axis value to 1-100.
yData = xData * xData # The y axis value will be X2 which will be upto 10000. 

plt.plot(xData,yData) # Plotting the x and y axis data
plt.show() # Running the plot.