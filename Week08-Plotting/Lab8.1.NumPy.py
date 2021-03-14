# A program that will generate 10 random numbers
# Author: Ryan Cox

import random
import numpy as np

lowestSalary = 2000
highestSalary = 8000
number = 10

randomSalaries = np.random.randint(lowestSalary, highestSalary, number)

print(randomSalaries)