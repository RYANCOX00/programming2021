# A program that will generate 10 random numbers
# Author: Ryan Cox

import numpy as np

lowestSalary = 2000
highestSalary = 8000
number = 10


np.random.seed(1) # Archoring the random numbers so that remain the same.
randomSalaries = np.random.randint(lowestSalary, highestSalary, number) # Saving ten numbers within the above range to an array. 

print(randomSalaries)