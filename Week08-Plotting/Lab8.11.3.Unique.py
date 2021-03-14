import numpy as np
import matplotlib.pyplot as plt

"An array of raw data i.e. unsorted and not counted."
a = np.array( ["apple", "apple","apple", "apple", "banana", "banana", "banana", "banana", "pear", "pear", "pear", "pear", "pear", "pear", "pear", "pear", "pear"])

#unique_elements is the name of the fruit.  counts_elements is the frequency.  return_counts=True just says yes to returning the count. 
unique_elements, counts_elements = np.unique(a, return_counts=True) #can shorten variable names if you wish.

#printing these two varaibles as seperate arrays
print(np.asarray((unique_elements, counts_elements)))

#counts as the contents of the pie and unique as the label
plt.pie(counts_elements, labels=unique_elements)
plt.show()