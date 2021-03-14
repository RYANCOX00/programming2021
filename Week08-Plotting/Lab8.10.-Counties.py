# A program that will show how many All-Ireland football titles the top counties have on a pie chart.
# Author: Ryan Cox

import numpy as np
import matplotlib.pyplot as plt


numTitles = np.array([37,30, 9, 7, 7])
counties = ("Kerry", "Dublin", "Galway", "Cork", "Meath")

plt.pie(numTitles, labels=counties)
plt.show()