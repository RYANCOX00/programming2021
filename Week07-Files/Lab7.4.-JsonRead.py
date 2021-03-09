# A program that will read in an object from a json file. 
# Author: Ryan Cox

import json

file = "records.json"

def readRecords():
    with open(file, "rt") as f:
        data = json.load(f)
    return data

data = readRecords()

print(data)