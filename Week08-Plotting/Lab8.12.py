import numpy as np
import matplotlib.pyplot as plt
# make the array of occurences
possibleCounties = ["Kerry", "Dublin", "Galway", "Cork", "Meath"]


# Random.choice() is a probability function.  First is the objects, then the probability of their frequency(p), 
# Size is the size of the sample.
# Frequency(p) must equal to one. 
counties = np.random.choice(possibleCounties, p=[0.37, 0.3, 0.13, 0.1, 0.1 ] ,size=(100))  


#unique_elements is the name of the counties.  counts_elements is their frequency.  return_counts=True says yes to returning the count. 
unique, counts = np.unique(counties, return_counts=True)

plt.bar(unique,counts)
plt.show()