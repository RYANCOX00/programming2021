# A program that will show how many people are on salaries within certain ranges. 
# Author: Ryan Cox

import numpy as np
import matplotlib.pyplot as plt

lowestSalary = 2000
highestSalary = 8000
number = 10


np.random.seed(1)
randomSalaries = np.random.randint(lowestSalary, highestSalary, number)

print(randomSalaries)
plt.hist(randomSalaries)
plt.show()